from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('dashboard/', views.BooksAvailability.as_view(), name='books_availability'),
    path('libraries/', views.Libraries.as_view(), name='libraries'),
    path('dashboard/remove/<int:pk>', views.BookRemove.as_view(), name='book_remove'),
    path('libraries/details/<int:pk>', views.LibrariesDetails.as_view(), name='libraries_details'),
    path('libraries/modify/<int:pk>', views.LibrariesModify.as_view(), name='libraries_modify'),
    path('libraries/add/', views.LibrariesAdd.as_view(), name='libraries_add'),
    path('libraries/remove/<int:pk>', views.LibrariesRemove.as_view(), name='libraries_remove'),
    path('dashboard/remove/', views.BookRemoveAll.as_view(), name='book_remove_all'),
    path('libraries/summary/<int:pk>', views.Summary.as_view(), name='summary'),
]