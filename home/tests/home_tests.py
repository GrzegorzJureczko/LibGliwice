from django.urls import reverse


def test_home_page(client, user):
    client.force_login(user)
    endpoint = reverse('home:home')
    response = client.get(endpoint)
    assert response.status_code == 200


def test_home_page_content(client, user):
    client.force_login(user)
    endpoint = reverse('home:home')
    response = client.get(endpoint)
    assert 'images/logo/logo.svg' in str(response.content.decode('UTF-8'))
