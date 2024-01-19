import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import User
from todo.models import Status


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="testemail@gmail.com", password="123456789ab", is_verified=True
    )
    return user


@pytest.fixture
def common_status():
    status = Status.objects.create(name="test")
    return status


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_data(common_user, common_status):
    data = {
        "author": common_user,
        "title": "test",
        "description": "test",
        "status": common_status,
    }
    return data


@pytest.fixture
def common_url():
    url = reverse("todo:api-v1:task-list")
    return url


@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_200_status(self, api_client, common_url):
        response = api_client.get(common_url)
        assert response.status_code == 401

    def test_create_post_response_201_status(
        self, api_client, common_data, common_url
    ):
        response = api_client.post(common_url, common_data)
        assert response.status_code == 401

    def test_create_post_response_201_status_with_login(
        self, api_client, common_user, common_data, common_url
    ):
        api_client.force_login(user=common_user)
        response = api_client.post(common_url, common_data)
        assert response.status_code == 201

    def test_create_post_response_force_authenticate(
        self, api_client, common_user, common_data, common_url
    ):
        api_client.force_authenticate(user=common_user)
        response = api_client.post(common_url, common_data)
        assert response.status_code == 201
