from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Libraries(models.Model):
    name = models.CharField(max_length=60, unique=True)
    short_name = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=30, default=None)
    email = models.EmailField(max_length=30, default=None)
    opening_time = models.CharField(max_length=500, default=None)


class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    status = models.ManyToManyField('Libraries', through='BooksLibraries')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class BooksLibraries(models.Model):
    library = models.ForeignKey('Libraries', on_delete=models.CASCADE)
    books = models.ForeignKey('Books', on_delete=models.CASCADE)
    status = models.IntegerField(choices=[
        (1, 'available'),
        (2, 'not_available'),
        (3, 'loan'),
    ])
    place = models.CharField(max_length=30)
