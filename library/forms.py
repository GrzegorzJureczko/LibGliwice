from django import forms

from . import models

class LibraryForm(forms.ModelForm):
    class Meta:
        model = models.Libraries
        fields = ('name', 'short_name', 'address', 'phone', 'email', 'opening_time')