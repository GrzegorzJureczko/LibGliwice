from django.shortcuts import render, redirect
from django.views import View
import requests
from bs4 import BeautifulSoup
from django.views.generic import ListView

from library import models


# Create your views here.
class Libraries(ListView):
    template_name = 'library/libraries.html'
    model = models.Libraries
    context_object_name = 'libraries'


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
        url = request.POST.get('link')
        response = requests.get(str(url))
        soup = BeautifulSoup(response.text, 'html.parser')
        branch = soup.find_all('b')
        title = soup.find('h1')
        author_sib = soup.find('dt', text='Tytuł pełny:')
        author = str(author_sib.next_sibling.next_sibling)

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

        # splitting branches and saving data to a list
        books_availability = []
        while len(branch) > 0:
            books_availability.append((branch[0].string, branch[1].string, branch[2].string))
            for i in range(3):
                branch.pop(0)

        # retrieving list of libraries by short name
        short_libraries_names = models.Libraries.objects.all()
        short_libraries_names_list = [item.short_name for item in short_libraries_names]

        # cleaning list, deleting double branches and children libraries
        clean_books_availability = []
        short_name_list = []
        for book in books_availability:
            if book[0] not in short_name_list and book[0] in short_libraries_names_list:
                clean_books_availability.append(book)
                short_name_list.append(book[0])

        # filling list with libraries where book is unavailable
        branch_list = [branch[0] for branch in clean_books_availability]
        for idx, item in enumerate(short_libraries_names_list):
            if item not in branch_list:
                clean_books_availability.insert(idx, (item, 'n/a', 'niedostępna'))

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



# https://integro.biblioteka.gliwice.pl/692300192868/twain-mark/pamietniki-adama-i-ewy?bibFilter=69'
# https://integro.biblioteka.gliwice.pl/693000398890/sabaliauskaite-kristina/silva-rerum-ii?bibFilter=69'
# https://integro.biblioteka.gliwice.pl/692700361185/zajdel-janusz-andrzej/limes-inferior?bibFilter=69'
# https://integro.biblioteka.gliwice.pl/692300152237/pacynski-tomasz/maskarada?bibFilter=69'
