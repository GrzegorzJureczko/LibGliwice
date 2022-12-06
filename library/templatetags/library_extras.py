from django import template

register = template.Library()

@register.filter
def in_books(status, book):
    return status.filter(books=book)
