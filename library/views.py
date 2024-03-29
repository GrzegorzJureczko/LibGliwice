from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
import requests
from bs4 import BeautifulSoup
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from library import models
from collection import models as c_models
from library.forms import LibraryCreateForm


# Create your views here.
class Libraries(ListView):
    # displays list of existing libraries
    template_name = 'library/libraries.html'
    model = models.Libraries
    context_object_name = 'libraries'


class LibrariesDetails(DetailView):
    # displays library's details
    model = models.Libraries
    context_object_name = 'library'
    template_name = 'library/library_details.html'


class LibrariesModify(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    # modifies library details, proper permission required
    model = models.Libraries
    context_object_name = 'library'
    fields = ('name', 'short_name', 'address', 'phone', 'email', 'opening_time')
    template_name = 'library/library_modify.html'
    success_url = reverse_lazy('library:libraries')
    permission_required = 'library.change_libraries'
    login_url = reverse_lazy('users:login')


class LibrariesAdd(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'library.add_libraries'

    def get(self, request):
        # displays library add form
        form = LibraryCreateForm()
        return render(request, 'library/library_add.html', context={'form': form})

    def post(self, request):
        # adds library, proper permission required
        form = LibraryCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            short_name = form.cleaned_data['short_name']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            opening_time = form.cleaned_data['opening_time']

            library = models.Libraries(name=name, short_name=short_name, address=address, phone=phone, email=email,
                                       opening_time=opening_time)
            library.save()

            # fills existing books with default data and save relation, needed for correct work with data already beeing used
            books = models.Books.objects.all()
            for book in books:
                books_library_relation = models.BooksLibraries(library=library, book=book, status=3,
                                                               location='n/a')
                books_library_relation.save()

            return redirect('library:libraries')
        return render(request, 'library/library_add.html', context={'form': form})


class LibrariesRemove(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    # removes library, proper permission required, confirmation required
    model = models.Libraries
    success_url = reverse_lazy('library:libraries')
    template_name = 'library/library_remove.html'
    permission_required = 'library.delete_libraries'
    login_url = reverse_lazy('users:login')


class BooksAvailability(View):
    # displays books related to libraries filtered for proper user. Only records desired by user
    def get(self, request):
        user = request.user
        libraries = models.Libraries.objects.all()
        books = models.Books.objects.filter(user=user.id)
        status = models.BooksLibraries.objects.all()

        books_len = len(books) + 1  # passes variable for js purpose. Book add to my library feature
        return render(request, 'library/dashboard.html',
                      context={'libraries': libraries, 'status': status, 'books': books, 'books_len': books_len})

    def post(self, request, url=None):
        # saves data of book availability in all libraries. Obtained data must be processed first
        user = request.user

        # retrieving data from library database about book availability using link provided by user
        try:
            if not url:  # checks if url is set by user or url comes with random urls from demo version
                url = request.POST.get('link')
            response = requests.get(str(url))
            soup = BeautifulSoup(response.text, 'html.parser')

            # retrieving book's branch, location and availability
            raw_branch_data = soup.find_all('dd')
            branch = []
            for line in raw_branch_data:
                for branch_item in line.find_all('b'):
                    branch.append(branch_item.string)

            # retrieving book's title
            title = soup.find('h1')
            title = title.string

            # retrieving author's name
            author_sib = soup.find('dt', text='Tytuł pełny:')
            author = str(author_sib.next_sibling.next_sibling)
            if ';' in author:
                auth = author[author.index('/') + 2:author.index(';')]
            else:
                auth = author[author.index('/') + 2:author.index('</')]

            # retrieving book's number of pages
            pages_sib = soup.find('dt', text='Opis fizyczny:')
            pages = str(pages_sib.next_sibling.next_sibling)
            if '[' in pages:
                pages = pages[pages.index('">') + 2:pages.index(',')]
            elif 'stron' in pages:
                pages = pages[pages.index('">') + 2:pages.index('stron')]
            else:
                pages = pages[pages.index('">') + 2:pages.index('s.') - 1]
            # leaves only digits
            pages = ''.join(c for c in pages if c.isdigit())

        except:
            return redirect('library:books_availability')

        # splitting branches and saving data to a list
        books_availability = []
        while len(branch) > 0:
            books_availability.append((branch[0].string, branch[1].string, branch[2].string))
            for i in range(3):
                branch.pop(0)

        # retrieving list of libraries by short name
        short_libraries_names_list = [item.short_name for item in models.Libraries.objects.all()]

        # cleaning list, deleting double branches and children libraries
        clean_books_availability = []
        temporary_short_name_list = []
        for book in books_availability:
            if book[0] not in temporary_short_name_list and book[0] in short_libraries_names_list:
                clean_books_availability.append(book)
                temporary_short_name_list.append(book[0])

        # filling list with libraries where book is unavailable
        branch_list = [branch[0] for branch in clean_books_availability]
        for item in short_libraries_names_list:
            if item not in branch_list:
                clean_books_availability.append((item, 'n/a', 'niedostępna'))

        # ordering by database pattern
        list_order_pattern = {}
        for idx, i in enumerate(short_libraries_names_list):
            list_order_pattern[i] = idx
        clean_books_availability.sort(key=lambda val: list_order_pattern[val[0]])

        # if book already exists, preparing data, updating relation
        if models.Books.objects.filter(name=title).exists():
            if models.Books.objects.filter(name=title, user=user).exists():
                for book in clean_books_availability:
                    library_short_name = book[0]
                    book_location = book[1]
                    book_status = book[2]

                    if book_status == 'dostępna':
                        book_status = 1
                    elif book_status == 'Wypożyczona':
                        book_status = 2
                    else:
                        book_status = 3

                    add_book = models.Books.objects.get(name=title)
                    library = models.Libraries.objects.get(short_name=library_short_name)
                    book_libraries_relation = models.BooksLibraries.objects.get(library=library, book=add_book)

                    if book_libraries_relation.status == 3:
                        book_libraries_relation.status = book_status
                    if book_libraries_relation.status == 2 and book_location == 1:
                        book_libraries_relation.status = book_status

                    book_libraries_relation.location = book_location
                    book_libraries_relation.save()

                    add_book.user.add(user)
            else:
                for book in clean_books_availability:
                    library_short_name = book[0]
                    book_location = book[1]
                    book_status = book[2]

                    if book_status == 'dostępna':
                        book_status = 1
                    elif book_status == 'Wypożyczona':
                        book_status = 2
                    else:
                        book_status = 3

                    add_book = models.Books.objects.get(name=title)
                    library = models.Libraries.objects.get(short_name=library_short_name)
                    book_libraries_relation = models.BooksLibraries.objects.get(library=library, book=add_book)
                    book_libraries_relation.status = book_status
                    book_libraries_relation.location = book_location
                    book_libraries_relation.save()

                    add_book.user.add(user)
        else:
            # if book doesn't exist, saving book
            add_book = models.Books(name=title, author=auth, pages=pages)
            add_book.save()

            # preparing data, establishing relation
            for book in clean_books_availability:
                library_short_name = book[0]
                book_location = book[1]
                book_status = book[2]

                if book_status == 'dostępna':
                    book_status = 1
                elif book_status == 'Wypożyczona':
                    book_status = 2
                else:
                    book_status = 3

                library = models.Libraries.objects.get(short_name=library_short_name)
                books_library_relation = models.BooksLibraries(library=library, book=add_book, status=book_status,
                                                               location=book_location)
                books_library_relation.save()

            add_book.user.add(user)

        return redirect('library:books_availability')


class BookRemove(View):
    # removes book availability data from dashboard indicated by user
    def get(self, request, pk):
        user = request.user
        book = models.Books.objects.get(pk=pk)
        book.user.remove(user)

        return redirect('library:books_availability')


class BookRemoveAll(View):
    # removes all books availability data from dashboard
    def get(self, request):
        user = request.user

        books = models.Books.objects.all()
        for book in books:
            book.user.remove(user)

        return redirect('library:books_availability')


class Summary(View):
    # shows library details with user's books of interest with accurate location. Only those which are available in this library
    def get(self, request, pk):
        user = request.user
        library = models.Libraries.objects.get(id=pk)
        books = models.Books.objects.filter(user=user.id, libraries=library, bookslibraries__status=1)
        status = models.BooksLibraries.objects.all()
        return render(request, 'library/summary.html', context={'library': library, 'books': books, 'status': status})
