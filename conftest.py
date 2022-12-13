import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.core.management import call_command
from django.urls import reverse
from collection import models as coll
from library import models



@pytest.fixture
def user(db):
    User = get_user_model()
    return User.objects.create(username='JohnyJohny', email='johnyjohny@gmail.com', password='TestPass123')


@pytest.fixture
def user2(db):
    User = get_user_model()
    return User.objects.create(username='Tommy', email='tommy@gmail.com', password='TestPass123')


@pytest.fixture
def library_create(db):
    return models.Libraries.objects.create(name='Filia 40', short_name='F40', address='ul. Polna 7',
                                           phone='554 778 889', email='filia40@gliwice.pl',
                                           opening_time='Poniedziałek 8:00-20:00')


@pytest.fixture
def book_create(db):
    return models.Books.objects.create(name='Diuna', author='Frank Herbert')


@pytest.fixture
def book_user_relation_create(db, user):
    library = models.Libraries.objects.create(name='Filia 40', short_name='F40', address='ul. Polna 7',
                                              phone='554 778 889', email='filia40@gliwice.pl',
                                              opening_time='Poniedziałek 8:00-20:00')
    book = models.Books.objects.create(name='Diuna', author='Frank Herbert')
    book2 = models.Books.objects.create(name='1984', author='George Orwell')
    book3 = models.Books.objects.create(name='Hobbit', author='J.R.R. Tolkien')
    models.BooksLibraries(library=library, book=book, status=1,
                          location='eng')

    book.user.add(user)
    book2.user.add(user)
    book3.user.add(user)


@pytest.fixture
def book_library_relation_create(db, user):
    library = models.Libraries.objects.create(name='Filia 40', short_name='F40', address='ul. Polna 7',
                                              phone='554 778 889', email='filia40@gliwice.pl',
                                              opening_time='Poniedziałek 8:00-20:00')
    book = models.Books.objects.create(name='Diuna', author='Frank Herbert')
    book2 = models.Books.objects.create(name='1984', author='George Orwell')
    book3 = models.Books.objects.create(name='Hobbit', author='J.R.R. Tolkien')
    models.BooksLibraries.objects.create(library=library, book=book, status=1,
                                         location='eng')
    models.BooksLibraries.objects.create(library=library, book=book2, status=2,
                                         location='eng')
    models.BooksLibraries.objects.create(library=library, book=book3, status=3,
                                         location='eng')
    book.user.add(user)
    book2.user.add(user)
    book3.user.add(user)


@pytest.fixture
def collection_relation(db, user):
    book = models.Books.objects.create(name='Diuna', author='Frank Herbert')
    book2 = models.Books.objects.create(name='1984', author='George Orwell')
    book3 = models.Books.objects.create(name='Hobbit', author='J.R.R. Tolkien')
    read_books_rel_1 = coll.ReadBooks.objects.create(book=book, date='2022-05-12', read=1)
    read_books_rel_2 = coll.ReadBooks.objects.create(book=book2, date='2020-03-15', read=1)
    read_books_rel_3 = coll.ReadBooks.objects.create(book=book3, date='2022-11-20', read=1)
    read_books_rel_1.users.add(user)
    read_books_rel_2.users.add(user)
    read_books_rel_3.users.add(user)