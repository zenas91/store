from rest_framework.test import APIClient
from django.contrib.auth.models import User
import pytest


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate_user(api_client):
    def authenticate(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))
    return authenticate
