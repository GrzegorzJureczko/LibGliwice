from django.urls import reverse
from collection import models
from library import models


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
    assert 200
