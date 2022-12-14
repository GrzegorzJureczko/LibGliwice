from django.urls import reverse
from collection import models
from library import models as lib


def test_mylibrary_display_correct_data(collection_relation, user, client):
    client.force_login(user)
    endpoint = reverse('collection:my_library')
    response = client.get(endpoint)
    assert 'Diuna' in str(response.content)
    assert 'George Orwell' in str(response.content)
    assert 'Nov. 20, 2022' in str(response.content)


def test_mylibrary_user_only_sees_own_data(collection_relation, user2, client):
    client.force_login(user2)
    endpoint = reverse('collection:my_library')
    response = client.get(endpoint)
    assert 'Diuna' not in str(response.content)
    assert 'George Orwell' not in str(response.content)
    assert 'Nov. 20, 2022' not in str(response.content)


def test_mylibrary_page(user, client):
    client.force_login(user)
    endpoint = reverse('collection:my_library')
    response = client.get(endpoint)
    assert response.status_code == 200


def test_book_collection_add_redirect(book_user_relation_create, user, client):
    client.force_login(user)
    endpoint = reverse('collection:book_collection_add', args=(1,))
    book = models.Books.objects.get(id=1)
    response = client.post(endpoint, data={'book': book, 'date': '2022-11-05', 'read': 1})
    read_books_rel = models.ReadBooks.objects.create(book=book, date='2022-05-12', read=1)
    read_books_rel.users.add(user)
    readbook = models.ReadBooks.objects.all()
    assert response.status_code == 302
    assert response.url.startswith('/collection/')


def test_book_collection_page(book_user_relation_create, user, client):
    client.force_login(user)
    endpoint = reverse('collection:book_collection_add', args=(1,))
    response = client.get(endpoint)
    assert "Data przeczytania" in str(response.content)


def test_collection_new_add_success(user, client):
    client.force_login(user)
    endpoint = reverse('collection:book_collection_add_new')
    response = client.post(endpoint, data={'title': 'Testamenty', 'author': 'Margaret Antwood', 'date': '2017-12-01',
                                           'user': 'user'})
    assert models.Books.objects.get(name='Testamenty')


def test_collection_new_add_page(user, client):
    client.force_login(user)
    endpoint = reverse('collection:book_collection_add_new')
    response = client.get(endpoint)
    assert response.status_code == 200


def test_collection_new_add_remove(user, client):
    client.force_login(user)
    endpoint = reverse('collection:book_collection_add_new')
    response = client.post(endpoint, data={'title': 'Testamenty', 'author': 'Margaret Antwood', 'date': '2017-12-01',
                                           'user': 'user'})
    books = models.ReadBooks.objects.all()
    assert len(books) == 1
    endpoint = reverse('collection:book_collection_remove', args=(1,))
    response = client.get(endpoint)
    books = models.ReadBooks.objects.all()
    assert len(books) == 0


def test_collection_new_add_redirect(user, client):
    client.force_login(user)
    endpoint = reverse('collection:book_collection_add_new')
    response = client.post(endpoint, data={'title': 'Testamenty', 'author': 'Margaret Antwood', 'date': '2017-12-01',
                                           'user': 'user'})
    endpoint = reverse('collection:book_collection_remove', args=(1,))
    response = client.get(endpoint)
    assert response.status_code == 302
