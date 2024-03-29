from django.shortcuts import render, redirect
from django.views import View
from library import models
from collection import models


# Create your views here.
class MyLibrary(View):
    def get(self, request):
        # displays books added by user marked as read
        user = request.user
        read_books = models.Books.objects.filter(readbooks__read=1, readbooks__users=user.id)
        date_read = models.ReadBooks.objects.all()

        return render(request, 'collection/mylibrary.html',
                      context={'books': read_books, 'date_read': date_read, 'user': user})


class BookCollectionAdd(View):
    def get(self, request, pk):
        # displays form collecting date of book been read. User and book details already provided and hidden.
        book = models.Books.objects.get(pk=pk)
        return render(request, 'collection/book_collection_add.html', context={'book': book})

        # adds connection m2m with user and readbook model what allows to make a list of books read by user
    def post(self, request, pk):
        user = request.user
        book = models.Books.objects.get(pk=pk)
        date = request.POST.get('date')

        if not models.Books.objects.filter(name=book, readbooks__users=user).exists():
            read = models.ReadBooks(book=book, date=date, read=1)
            read.save()
            read.users.add(user)
            book.user.remove(user)

        return redirect('collection:my_library')


class BookCollectionAddNew(View):
    def get(self, request):
        # displays form to add book marked as read which is not present on dashboard site
        return render(request, 'collection/book_collection_add_new.html')

    def post(self, request, random_book=None):
        # saves data of new book and establishes connection in readbook model
        user = request.user
        if not random_book:
            title = request.POST.get('title')
            author = request.POST.get('author')
            date = request.POST.get('date')
        else:
            title = random_book['title']
            author = random_book['author']
            date = random_book['date']


        if not models.Books.objects.filter(name=title, author=author).exists():
            book = models.Books(name=title, author=author)
            book.save()
            read = models.ReadBooks(book=book, date=date, read=1)
            read.save()
            read.users.add(user)
        else:
            book = models.Books.objects.get(name=title, author=author)
            read = models.ReadBooks(book=book, date=date, read=1)
            read.save()
            read.users.add(user)
        return redirect('collection:my_library')


class BookCollectionRemove(View):
    def get(self, request, pk):
        # removes book from books read by user
        user = request.user
        book = models.Books.objects.get(pk=pk)
        models.ReadBooks.objects.get(users=user, book=book).delete()

        return redirect('collection:my_library')
