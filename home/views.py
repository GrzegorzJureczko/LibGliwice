from bs4 import BeautifulSoup
from django.contrib.sites import requests
from django.shortcuts import render
from django.views import View
import requests


# Create your views here.

class home(View):
    def get(self, request):

        url = 'https://integro.biblioteka.gliwice.pl/693000398890/sabaliauskaite-kristina/silva-rerum-ii?bibFilter=69'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        res = soup.find_all('b')

        # # dict = defaultdict(list)
        # # for i in res:
        #
        #
        # print(list)

        list = [i.string for i in res]

        print(list)

        return render(request, 'home/home.html', context={'list':list})
