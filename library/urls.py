from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('dashboard/', views.Books_availability.as_view(), name='books_availability'),
    path('libraries/', views.Libraries.as_view(), name='libraries'),
    
]