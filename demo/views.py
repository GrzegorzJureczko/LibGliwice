import random

from django.shortcuts import render, redirect
from django.views import View

from library import views as l_views
from collection import views as c_views

from demo.sample_books import SAMPLE_BOOKS, random_availability
from library import models as l_models
from collection import models as c_models


class DemoVersion(View):
    # clears all data and populate with new for demo purpose
    def get(self, request):
        l_views.BookRemoveAll().get(request)
        sample_books = SAMPLE_BOOKS[:]
        random.shuffle(sample_books)

        for title, author, pages in sample_books[:5]:
            l_views.BooksAvailability().save_availability(
                request.user, title, author, pages, random_availability())

        user = request.user
        books = l_models.Books.objects.filter(readbooks__users=user)
        for book in books:
            c_models.ReadBooks.objects.get(users=user, book=book).delete()


        random_books = [
            {'title': 'Duma i uprzedzenie', 'author': 'Jane Austen', 'date': '2023-02-09'},
            {'title': 'Wielkie nadzieje', 'author': 'Charles Dickens', 'date': '2023-01-01'},
            {'title': 'Jane Eyre', 'author': 'Charlotte Bronte', 'date': '2022-12-19'},
            {'title': 'Tessa D’Urberville', 'author': 'Thomas Hardy', 'date': '2021-04-22'},
            {'title': 'Rebeka', 'author': 'Daphne Du Maurier', 'date': '2022-05-24'},
            {'title': 'Buszujący w zbożu', 'author': 'JD Salinger', 'date': '2019-07-24'},
            {'title': 'Znowu w Brideshead', 'author': 'Evelyn Waugh', 'date': '2022-10-13'},
            {'title': 'Zbrodnia i kara', 'author': 'Fyodor Dostoyevsky', 'date': '2022-11-30'},
            {'title': 'Nędznicy', 'author': 'Victor Hugo', 'date': '2020-05-31'},
            {'title': 'Charlie i fabryka czekolady', 'author': 'Roald Dahl', 'date': '2018-08-12'},
            {'title': 'Hamlet', 'author': 'William Shakespeare', 'date': '2021-07-22'},
            {'title': 'Trzej muszkieterowie', 'author': 'Alexandre Dumas', 'date': '2023-01-21'},
            {'title': 'Miasteczko jak Alece Springs', 'author': 'Nevil Shute', 'date': '2020-02-04'},
            {'title': 'Wodnikowe Wzgórze', 'author': 'Richard Adams', 'date': '2021-11-27'},
            {'title': 'Fabryka os', 'author': 'Iain Banks', 'date': '2019-12-31'},
            {'title': 'Mały Książę', 'author': 'Antoine De Saint-Exupery', 'date': '2020-06-30'},
            {'title': 'Jądro ciemności', 'author': 'Joseph Conrad', 'date': '2021-09-30'},
            {'title': 'The Faraway Tree Collection', 'author': 'Enid Blyton', 'date': '2020-03-31'},
            {'title': 'Enid Blyton', 'author': 'Rohinton Mistry', 'date': '2021-04-07'},
            {'title': 'Pani Bovary', 'author': 'Gustave Flaubert', 'date': '2019-06-01'},
            {'title': 'Okruchy dnia', 'author': 'Kazuo Ishiguro', 'date': '2019-01-31'},
            {'title': 'Kolor purpury', 'author': 'Alice Walker', 'date': '2021-02-04'},
        ]
        random.shuffle(random_books)

        for random_book in random_books[:5]:
            c_views.BookCollectionAddNew().post(request, random_book)

        return redirect('library:books_availability')
