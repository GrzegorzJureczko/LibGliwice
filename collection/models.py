from django.contrib.auth.models import User
from django.db import models
from library.models import Books

class ReadBooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    date = models.DateField()


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    books = models.ManyToManyField(Books)
