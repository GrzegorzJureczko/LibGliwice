from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
import requests
from bs4 import BeautifulSoup
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from library import models


# Create your views here.
class Libraries(ListView):
    # shows list of existing libraries
    template_name = 'library/libraries.html'
    model = models.Libraries
    context_object_name = 'libraries'


# class LibrariesDetails(View):
#     # shows library's details
#     def get(self, request, id):
#         library = models.Libraries.objects.get(id=id)
#         return render(request, 'library/library_details.html', context={'library': library})

class LibrariesDetails(DetailView):
    # shows library's details
    model = models.Libraries
    context_object_name = 'library'
    template_name = 'library/library_details.html'


class LibrariesModify(UpdateView, PermissionRequiredMixin):
    # modyfies Library
    model = models.Libraries
    context_object_name = 'library'
    fields = ('name', 'short_name', 'address', 'phone', 'email', 'opening_time')
    template_name = 'library/library_modify.html'
    success_url = reverse_lazy('library:libraries')
    permission_required = 'library.change_libraries'


class LibrariesAdd(CreateView, PermissionRequiredMixin):
    # Adds Library
    model = models.Libraries
    fields = ('name', 'short_name', 'address', 'phone', 'email', 'opening_time')
    template_name = 'library/library_add.html'
    success_url = reverse_lazy('library:libraries')
    permission_required = 'library.add_libraries'


class LibrariesRemove(DeleteView):
    model = models.Libraries
    success_url = reverse_lazy('library:libraries')
    template_name = 'library/library_remove.html'


class Books_availability(View):
    def get(self, request):
        user = request.user
        try:
            libraries = models.Libraries.objects.all()
            books = models.Books.objects.filter(user_id=user.id)
            status = models.BooksLibraries.objects.all()
        except:
            return render(request, 'library/dashboard.html')

        return render(request, 'library/dashboard.html',
                      context={'libraries': libraries, 'status': status, 'books': books})

    def post(self, request):
        user = request.user

        # retrieving from library database data about book availability using link provided by user
        try:
            url = request.POST.get('link')
            response = requests.get(str(url))
            soup = BeautifulSoup(response.text, 'html.parser')
            branch = soup.find_all('b')
            title = soup.find('h1')
            author_sib = soup.find('dt', text='Tytuł pełny:')
            author = str(author_sib.next_sibling.next_sibling)
        except:
            return redirect('library:books_availability')

        # retrieving book's author and title
        title = title.string
        if ';' in author:
            auth = ''
            for idx in range(author.index('/') + 2, author.index(';')):
                auth = auth + author[idx]
        else:
            auth = ''
            for idx in range(author.index('/') + 2, author.index('</')):
                auth = auth + author[idx]

        # checks book exists
        if models.Books.objects.filter(name=title, user_id=user.id).exists():
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
        for idx, item in enumerate(short_libraries_names_list):
            if item not in branch_list:
                clean_books_availability.insert(idx, (item, 'n/a', 'niedostępna'))

        # ordering by database pattern
        list_order_pattern = {}
        for idx, i in enumerate(short_libraries_names_list):
            list_order_pattern[i] = idx
        clean_books_availability.sort(key=lambda val: list_order_pattern[val[0]])

        # saving book
        add_book = models.Books(name=title, author=auth, user_id=user.id)
        add_book.save()

        # establishing relations and saving location and status
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
            relation = models.BooksLibraries(library=library, book=add_book, status=book_status, location=book_location)
            relation.save()

        return redirect('library:books_availability')


class BookRemove(View):
    def get(self, request, id):
        book = models.Books.objects.get(id=id)
        book.delete()
        return redirect('library:books_availability')


class BookRemoveAll(View):
    def get(self, request):
        user = request.user
        books = models.Books.objects.filter(user_id=user.id)
        books.delete()
        return redirect('library:books_availability')

# https://integro.biblioteka.gliwice.pl/692300192868/twain-mark/pamietniki-adama-i-ewy?bibFilter=69'
# https://integro.biblioteka.gliwice.pl/693000398890/sabaliauskaite-kristina/silva-rerum-ii?bibFilter=69'
# https://integro.biblioteka.gliwice.pl/692700361185/zajdel-janusz-andrzej/limes-inferior?bibFilter=69'
# https://integro.biblioteka.gliwice.pl/692300152237/pacynski-tomasz/maskarada?bibFilter=69'
