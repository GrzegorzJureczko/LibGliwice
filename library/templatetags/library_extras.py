from django import template

register = template.Library()


@register.filter
def in_books(status, book):
    return status.filter(book=book)


@register.filter
def in_libraries(status, library):
    return status.filter(library=library)


@register.filter
def in_users(readbooks, user):
    return readbooks.filter(users=user)
