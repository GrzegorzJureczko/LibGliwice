from django.shortcuts import render, redirect
from django.views import View
from library import models
from collection import models


# Create your views here.
class MyLibrary(View):
    def get(self, request):
        user = request.user
        print(user)
        print(user.id)
        read_books = models.Books.objects.filter(readbooks__read=1, readbooks__users=user.id)
        # user_id=user.id, readbooks__read=1)

        return render(request, 'collection/mylibrary.html', context={'books': read_books})


# context={'books':read_books}

class BookCollectionAdd(View):
    def get(self, request, pk):
        book = models.Books.objects.get(pk=pk)
        return render(request, 'collection/book_collection_add.html', context={'book': book})

    def post(self, request, pk):
        user = request.user
        book = models.Books.objects.get(pk=pk)
        date = request.POST.get('date')
        read = models.ReadBooks(book=book, date=date, read=1)
        read.save()
        read.users.add(user)

        return redirect('collection:my_library')


class BookCollectionRemove(View):
    def get(self, request):

        return redirect('collection:my_library')


    # def post(self, request, pk):
    #     user = request.user
    #     book = models.Books.objects.get(pk=pk)
    #     date = request.POST.get('date')
    #     if not models.ReadBooks.objects.filter(book=book, date=date, read=1).exists():
    #         read = models.ReadBooks(book=book, date=date, read=1)
    #         read.save()
    #     else:
    #         read = models.ReadBooks.objects.get(book=book, date=date, read=1)
    #         read.users.add(user)