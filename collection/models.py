from django.contrib.auth.models import User
from django.db import models
from library.models import Books

class ReadBooks(models.Model):
    users = models.ManyToManyField(User)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    date = models.DateField()
    read = models.BooleanField(default=0)

    # def __str__(self):
    #     return self.book

class Collection(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    books = models.ManyToManyField(Books)
