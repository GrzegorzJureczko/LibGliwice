import random

from django.shortcuts import render, redirect
from django.views import View

from library import views as l_views
from collection import views as c_views

from library import models as l_models
from collection import models as c_models
from django.http import JsonResponse


class UrlCountView(View):
    # progress counter for generating new data
    def get(self, request):
        user = request.user
        books = l_models.Books.objects.filter(user=user.id)
        count = books.count()
        return JsonResponse({'context': count}, safe=False)


class DemoVersion(View):
    # clears all data and populate with new for demo purpose
    def get(self, request):
        l_views.BookRemoveAll().get(request)
        urls = [
            'https://integro.biblioteka.gliwice.pl/692300192868/twain-mark/pamietniki-adama-i-ewy?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692700361185/zajdel-janusz-andrzej/limes-inferior?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692300149008/grochulska-barbara/male-panstwo-wielkich-nadziei?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692300305243/niffenegger-audrey/zona-podroznika-w-czasie?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692300021899/adams-douglas/autostopem-przez-galaktyke?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692300303408/welborn-amy/zrozumiec-kod-da-vinci?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692300248008/garcia-marquez-gabriel/sto-lat-samotnosci?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692600349859/hardy-thomas/z-dala-od-zgielku?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692300037295/pille-lolita/bubble-gum?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692600349576/tartt-donna/tajemna-historia?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692300237958/roberts-gregory-david/shantaram?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692300181878/wiggs-susan/obudzic-szczescie?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692300295849/tennant-emma/zakochana-emma?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692300074599/tennant-emma/dziwne-losy-adelki?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692700357102/yanagihara-hanya/male-zycie?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/692900383434/fraczyk-izabella/za-stare-grzechy?bibFilter=69',
            'https://integro.biblioteka.gliwice.pl/693400489646/gren-hanna/piec-i-pol-smierci?bibFilter=69',
        ]
        random.shuffle(urls)

        count = 0
        for url in urls[:5]:
            # UrlCountView().get(request, count)
            l_views.BooksAvailability().post(request, url)

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
