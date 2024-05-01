from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from users import models


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("users:login")
    template_name = "registration/signup.html"


class UserAccount(View):
    def get(self, request):
        return render(request, 'registration/account.html')

class AutoLogin(View):
    def get(self, request):
        username = "demo"
        password = "TestPass123"

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log in the user
            login(request, user)
        return render(request, 'library/dashboard.html')
