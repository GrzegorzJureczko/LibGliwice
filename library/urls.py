from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('dashboard/', views.Books_availability.as_view(), name='books_availability'),
    path('libraries/', views.Libraries.as_view(), name='libraries'),
    path('dashboard/remove/<int:id>', views.BookRemove.as_view(), name='bookremove'),

]