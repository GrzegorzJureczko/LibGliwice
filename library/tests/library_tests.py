from django.contrib.auth.models import Permission
from django.urls import reverse
from library import models


def test_libraries_page(client, user):
    client.force_login(user)
    endpoint = reverse('library:libraries')
    response = client.get(endpoint)
    assert response.status_code == 200


def test_libraries_page_content(client, user):
    client.force_login(user)
    endpoint = reverse('library:libraries')
    response = client.get(endpoint)
    assert 'Dodaj filię' in str(response.content.decode('UTF-8'))


def test_libraries_details_page(client, library_create):
    endpoint = reverse('library:libraries_details', args=(1,))
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'godziny otwarcia:' in str(response.content)


def test_libraries_details_relate_to_correct_library(client, library_create):
    endpoint = reverse('library:libraries_details', args=(1,))
    response = client.get(endpoint)
    assert 'filia40@gliwice.pl' in str(response.content)


def test_libraries_details_modifies_success(client, user, library_create):
    client.force_login(user)
    permission = Permission.objects.get(name='Can change libraries')
    user.user_permissions.add(permission)
    endpoint = reverse('library:libraries_modify', args=(1,))
    response = client.post(endpoint, data={'name': 'Filia 45', 'short_name': 'F45', 'address': 'ul. Żwirowa 4',
                                           'phone': '458 741 474', 'email': 'filia45@gliwice.pl',
                                           'opening_time': 'Poniedziałek 8:00-20:00, Wtorek 10:30-20:00'})
    lib = models.Libraries.objects.get(email='filia45@gliwice.pl')
    assert lib.email == 'filia45@gliwice.pl'


def test_libraries_details_modifies_without_permission_fail(client, library_create, user):
    endpoint = reverse('library:libraries_modify', args=(1,))
    response = client.post(endpoint, data={'name': 'Filia 45', 'short_name': 'F45', 'address': 'ul. Żwirowa 4',
                                           'phone': '458 741 474', 'email': 'filia45@gliwice.pl',
                                           'opening_time': 'Poniedziałek 8:00-20:00, Wtorek 10:30-20:00'})
    lib = models.Libraries.objects.get(email='filia40@gliwice.pl')
    assert lib.email == 'filia40@gliwice.pl'


def test_library_add_success(client, user):
    client.force_login(user)
    permission = Permission.objects.get(name='Can add libraries')
    user.user_permissions.add(permission)
    endpoint = reverse('library:libraries_add')
    response = client.post(endpoint, data={'name': 'Filia 40', 'short_name': 'F40', 'address': 'ul. Polna 7',
                                           'phone': '554 778 889', 'email': 'filia40@gliwice.pl',
                                           'opening_time': 'Poniedziałek 8:00-20:00'})
    assert models.Libraries.objects.get(name='Filia 40')


def test_library_add_without_permission_fail(client, user):
    endpoint = reverse('library:libraries_add')
    response = client.post(endpoint, data={'name': 'Filia 40', 'short_name': 'F40', 'address': 'ul. Polna 7',
                                           'phone': '554 778 889', 'email': 'filia40@gliwice.pl',
                                           'opening_time': 'Poniedziałek 8:00-20:00'})
    library = models.Libraries.objects.all()
    assert len(library) == 0


def test_library_add_duplicate_fail(client, user, library_create):
    client.force_login(user)
    permission = Permission.objects.get(name='Can add libraries')
    user.user_permissions.add(permission)
    endpoint = reverse('library:libraries_add')
    response = client.post(endpoint, data={'name': 'Filia 40', 'short_name': 'F40', 'address': 'ul. Żwirowa 4',
                                           'phone': '458 741 474', 'email': 'filia45@gliwice.pl',
                                           'opening_time': 'Poniedziałek 8:00-20:00, Wtorek 10:30-20:00'})
    library = models.Libraries.objects.all()
    assert len(library) == 1


def test_library_remove_page(client, user, library_create):
    client.force_login(user)
    permission = Permission.objects.get(name='Can delete libraries')
    user.user_permissions.add(permission)
    endpoint = reverse('library:libraries_remove', args=(1,))
    response = client.get(endpoint)
    assert response.status_code == 200


def test_library_remove_success(client, user, library_create):
    client.force_login(user)
    permission = Permission.objects.get(name='Can delete libraries')
    user.user_permissions.add(permission)
    endpoint = reverse('library:libraries_remove', args=(1,))
    response = client.post(endpoint)
    library = models.Libraries.objects.all()
    assert len(library) == 0


def test_book_availability_page(client, user):
    client.force_login(user)
    endpoint = reverse('library:books_availability')
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'INTEGRO' in str(response.content.decode('UTF-8'))


def test_book_availability_form_success(client, user):
    client.force_login(user)
    endpoint = reverse('library:books_availability')
    response = client.post(endpoint, data={
        'link': 'https://integro.biblioteka.gliwice.pl/692300192868/twain-mark/pamietniki-adama-i-ewy?bibFilter=69'})
    response = client.post(endpoint, data={
        'link': 'https://integro.biblioteka.gliwice.pl/692700361185/zajdel-janusz-andrzej/limes-inferior?bibFilter=69'})
    response = client.post(endpoint, data={
        'link': 'https://integro.biblioteka.gliwice.pl/692300059720/herbert-frank/diuna?bibFilter=69'})
    books = models.Books.objects.all()
    assert len(books) == 3


def test_book_availability_form_fail(client, user):
    client.force_login(user)
    endpoint = reverse('library:books_availability')
    response = client.post(endpoint, data={
        'link': 'incorrect link'})
    books = models.Books.objects.all()
    assert len(books) == 0


def test_book_availability_form_duplicate(client, user):
    client.force_login(user)
    endpoint = reverse('library:books_availability')
    response = client.post(endpoint, data={
        'link': 'https://integro.biblioteka.gliwice.pl/692300192868/twain-mark/pamietniki-adama-i-ewy?bibFilter=69'})
    response = client.post(endpoint, data={
        'link': 'https://integro.biblioteka.gliwice.pl/692300192868/twain-mark/pamietniki-adama-i-ewy?bibFilter=69'})
    books = models.Books.objects.all()
    assert len(books) == 1


def test_book_remove_fail(client, user, book_user_relation_create):
    client.force_login(user)
    endpoint = reverse('library:book_remove', args=(1,))
    response = client.get(endpoint)
    assert response.status_code == 302


def test_book_remove_success_redirect(client, user, book_user_relation_create):
    client.force_login(user)
    endpoint = reverse('library:book_remove', args=(1,))
    response = client.get(endpoint)
    assert response.status_code == 302
    assert response.url.startswith('/dashboard/')


def test_book_remove_success(client, user, book_user_relation_create):
    client.force_login(user)
    book = models.Books.objects.get(name='Diuna')
    relation = models.Books.objects.get(user=user.id, name=book)
    assert relation
    endpoint = reverse('library:book_remove', args=(1,))
    response = client.get(endpoint)
    book.user.remove(user)
    assert len(models.Books.objects.filter(user=user.id)) == 2


def test_book_remove_wrong_user_fail(client, user, user2, book_user_relation_create):
    client.force_login(user2)
    book = models.Books.objects.get(name='Diuna')
    relation = models.Books.objects.get(user=user.id, name=book)
    assert relation
    endpoint = reverse('library:book_remove', args=(1,))
    response = client.get(endpoint)
    book.user.remove(user2)
    assert len(models.Books.objects.filter(user=user.id)) == 3


def test_book_remove_all_success_redirect(client, user, book_user_relation_create):
    client.force_login(user)
    endpoint = reverse('library:book_remove_all')
    response = client.get(endpoint)
    assert response.status_code == 302
    assert response.url.startswith('/dashboard/')


def test_book_remove_all_success(client, user, book_user_relation_create):
    client.force_login(user)
    books = models.Books.objects.all()
    endpoint = reverse('library:book_remove_all')
    response = client.get(endpoint)
    for book in books:
        book.user.remove(user)
    assert len(models.Books.objects.filter(user=user.id)) == 0


def test_summary_page(client, library_create):
    endpoint = reverse('library:summary', args=(1,))
    response = client.get(endpoint)
    assert 'filia40@gliwice.pl' in str(response.content)
    assert response.status_code == 200


def test_summary_page_displays_correct_data(client, user, book_library_relation_create):
    client.force_login(user)
    endpoint = reverse('library:summary', args=(1,))
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'Diuna' in str(response.content)
    assert '1984' not in str(response.content)
    assert 'eng' in str(response.content)
