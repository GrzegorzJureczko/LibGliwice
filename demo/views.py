import random

from django.shortcuts import render, redirect
from django.views import View

from library import views as l_views



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
        ]
        random.shuffle(urls)

        for url in urls[:5]:
            l_views.BooksAvailability().post(request, url)



        return redirect('library:books_availability')
