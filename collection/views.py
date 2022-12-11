from django.shortcuts import render, redirect
from django.views import View
from library import models
from collection import models


# Create your views here.
class MyLibrary(View):
    def get(self, request):
        user = request.user
        read_books = models.Books.objects.filter(readbooks__read=1, readbooks__users=user.id)
        date_read = models.ReadBooks.objects.all()

        return render(request, 'collection/mylibrary.html',
                      context={'books': read_books, 'date_read': date_read, 'user': user})


class BookCollectionAdd(View):
    def get(self, request, pk):
        book = models.Books.objects.get(pk=pk)
        return render(request, 'collection/book_collection_add.html', context={'book': book})

    def post(self, request, pk):
        user = request.user
        book = models.Books.objects.get(pk=pk)
        date = request.POST.get('date')
        if not models.Books.objects.filter(name=book, readbooks__users=user).exists():
            read = models.ReadBooks(book=book, date=date, read=1)
            read.save()
            read.users.add(user)

        return redirect('collection:my_library')


class BookCollectionAddNew(View):
    def get(self, request):
        return render(request, 'collection/book_collection_add_new.html')

    def post(self, request):
        user = request.user
        title = request.POST.get('title')
        author = request.POST.get('author')
        date = request.POST.get('date')
        if not models.Books.objects.filter(name=title, author=author).exists():
            book = models.Books(name=title, author=author)
            book.save()
            read = models.ReadBooks(book=book, date=date, read=1)
            read.save()
            read.users.add(user)
        return redirect('collection:my_library')


class BookCollectionRemove(View):
    def get(self, request, pk):
        user = request.user
        book = models.Books.objects.get(pk=pk)
        models.ReadBooks.objects.get(users=user, book=book).delete()

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
