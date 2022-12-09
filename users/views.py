from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("users:login")
    template_name = "registration/signup.html"


class UserAccount(View):
    def get(self, request):
        return render(request, 'registration/account.html')
