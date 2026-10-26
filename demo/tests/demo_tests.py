from django.urls import reverse

from library import models


def test_demo_populates_books_without_catalog_requests(client, user, monkeypatch):
    def fail_on_request(*args, **kwargs):
        raise AssertionError('demo must not call the catalog')

    monkeypatch.setattr('library.views.requests.get', fail_on_request)
    models.Libraries.objects.create(name='Filia 40', short_name='F40', address='ul. Polna 7',
                                    phone='554 778 889', email='filia40@gliwice.pl',
                                    opening_time='Poniedziałek 8:00-20:00')
    client.force_login(user)

    response = client.get(reverse('demo:demo'))

    assert response.status_code == 302
    assert models.Books.objects.filter(user=user).count() == 5
