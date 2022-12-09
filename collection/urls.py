from django.urls import path

from . import views

app_name = 'collection'

urlpatterns = [
    path('collection/mylibrary', views.MyLibrary.as_view(), name='my_library'),
    path('collection/bookadd/<int:pk>', views.BookCollectionAdd.as_view(), name='book_collection_add'),
    path('collection/bookremove/<int:pk>', views.BookCollectionRemove.as_view(), name='book_collection_remove'),

]