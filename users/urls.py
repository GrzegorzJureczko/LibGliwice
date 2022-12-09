from django.urls import path, include

from . import views
from . import views

app_name = 'users'

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("account/", views.UserAccount.as_view(), name="user_account"),

]