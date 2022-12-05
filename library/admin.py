from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Libraries)
admin.site.register(models.Books)
admin.site.register(models.BooksLibraries)