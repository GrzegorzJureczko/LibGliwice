import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

@pytest.fixture
def user(db):
    User = get_user_model()
    return User.objects.create(username='JohnyJohny', email='johnyjohny@gmail.com', password='TestPass123')


@pytest.mark.django_db
def test_create_user(user, django_user_model):
    users = django_user_model.objects.all()
    assert len(users) == 1


def test_change_password(user):
    user.set_password('Secret123')
    assert user.check_password('Secret123') is True


def test_login_page(client):
    endpoint = reverse('users:login')
    response = client.get(endpoint)
    assert response.status_code == 200
    assert '<h2>Login</h2>' in str(response.content)