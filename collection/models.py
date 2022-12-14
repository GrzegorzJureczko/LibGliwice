from django.contrib.auth.models import User
from django.db import models
from library.models import Books


class ReadBooks(models.Model):
    users = models.ManyToManyField(User)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    date = models.DateField()
    read = models.BooleanField(default=0)
