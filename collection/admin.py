from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.ReadBooks)
admin.site.register(models.Collection)