from django.shortcuts import render
from django.views import View
import requests


# Create your views here.

class home(View):
    # displays home page
    def get(self, request):
        return render(request, 'home/home.html')


class instruction(View):
    # displays instruction
    def get(self, request):
        return render(request, 'home/instruction.html')
