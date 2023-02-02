from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Libraries(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name='nazwa')
    short_name = models.CharField(max_length=10, unique=True, verbose_name='skrócona nazwa')
    address = models.CharField(max_length=150, verbose_name='adres')
    phone = models.CharField(max_length=30, default=None, verbose_name='telefon')
    email = models.EmailField(max_length=30, default=None)
    opening_time = models.CharField(max_length=500, default=None, verbose_name='godziny otwarcia')

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField(default=0)
    libraries = models.ManyToManyField('Libraries', through='BooksLibraries')
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class BooksLibraries(models.Model):
    library = models.ForeignKey('Libraries', on_delete=models.CASCADE)
    book = models.ForeignKey('Books', on_delete=models.CASCADE)
    status = models.IntegerField(choices=[
        (1, 'available'),
        (2, 'not_available'),
        (3, 'loan'),
    ])
    location = models.CharField(max_length=30)
