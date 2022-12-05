
from django.shortcuts import render
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
    # def get(self, request):
    #     return render(request, 'library/libraries.html')




class Books_availability(View):
    def get(self, request):
        return render(request, 'library/dashboard.html')

    def post(self, request):

        url = request.POST.get('link')
        response = requests.get(str(url))
        soup = BeautifulSoup(response.text, 'html.parser')
        branch = soup.find_all('b')
        title = soup.find('h1')
        author_sib = soup.find('dt', text='Tytuł pełny:')
        author = str(author_sib.next_sibling.next_sibling)

        if ';' in author:
            auth = ''
            for idx in range(author.index('/') + 2, author.index(';')):
                auth = auth + author[idx]
        else:
            auth = ''
            for idx in range(author.index('/') + 2, author.index('</')):
                auth = auth + author[idx]


        books_availability = [(title.string, auth)]
        while len(branch) > 0:
            books_availability.append((branch[0].string, branch[1].string, branch[2].string))
            for i in range(3):
                branch.pop(0)

     #   return books_availability

        return render(request, 'library/dashboard.html', context={'books_availability': books_availability})


# https://integro.biblioteka.gliwice.pl/692300192868/twain-mark/pamietniki-adama-i-ewy?bibFilter=69'
# https://integro.biblioteka.gliwice.pl/693000398890/sabaliauskaite-kristina/silva-rerum-ii?bibFilter=69'
# https://integro.biblioteka.gliwice.pl/692700361185/zajdel-janusz-andrzej/limes-inferior?bibFilter=69'
# https://integro.biblioteka.gliwice.pl/692300152237/pacynski-tomasz/maskarada?bibFilter=69'