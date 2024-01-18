import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import User


# Fixture to create a common user with verified status
@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="testemail@gmail.com", password="123456789ab", is_verified=True
    )
    return user


# Fixture to create an API client
@pytest.fixture
def api_client():
    client = APIClient()
    return client


# Fixture to create common data for testing
@pytest.fixture
def common_data(common_user):
    data = {
        "author": common_user,
        "title": "test",
        "description": "test",
        "status": "test",
    }
    return data


# Fixture to get the common URL
@pytest.fixture
def common_url():
    url = reverse("todo:api-v1:task-list")
    return url


# Test class for POST API tests
@pytest.mark.django_db
class TestPostApi:
    # Test for getting a post response with a 200 status code
    def test_get_post_response_200_status(self, api_client, common_url):
        response = api_client.get(common_url)
        assert response.status_code == 200

    # Test for creating a post response with a 201 status code (without login)
    def test_create_post_response_201_status(
        self, api_client, common_data, common_url
    ):
        response = api_client.post(common_url, common_data)
        assert response.status_code == 401

    # Test for creating a post response with a 201 status code (with login)
    def test_create_post_response_201_status_with_login(
        self, api_client, common_user, common_data, common_url
    ):
        api_client.force_login(user=common_user)
        response = api_client.post(common_url, common_data)
        assert response.status_code == 201

    # Test for creating a post response with force authentication (with login)
    def test_create_post_response_force_authenticate(
        self, api_client, common_user, common_data, common_url
    ):
        api_client.force_login(user=common_user)
        api_client.force_authenticate(user=common_user)
        # api_client.force_authenticate(user={})
        response = api_client.post(common_url, common_data)
        assert response.status_code == 401
