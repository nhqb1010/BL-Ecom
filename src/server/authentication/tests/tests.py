from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
import pytest

from app.errors.error_codes import AuthErrorCodes
from app.errors.exceptions import AppAuthException


User = get_user_model()


# ** Login Tests **
@pytest.mark.django_db
def test_auth_login_failed_cuz_wrong_password():
    User.objects.create_user(email="test@gmail.com", password="password")

    client = APIClient()
    response = client.post(reverse("token_obtain_pair"), {"email": "test@gmail.com", "password": "wrong_password"})

    assert response.status_code == AppAuthException.status_code
    assert response.data["error_code"] == AuthErrorCodes.INVALID_LOGIN_CREDENTIALS.name
    assert response.data["error_message"] == AuthErrorCodes.INVALID_LOGIN_CREDENTIALS.value


@pytest.mark.django_db
def test_auth_login_failed_cuz_wrong_email():
    User.objects.create_user(email="test@gmail.com", password="password")

    client = APIClient()
    response = client.post(reverse("token_obtain_pair"), {"email": "test1@gmail.com", "password": "password"})

    assert response.status_code == AppAuthException.status_code
    assert response.data["error_code"] == AuthErrorCodes.INVALID_LOGIN_CREDENTIALS.name
    assert response.data["error_message"] == AuthErrorCodes.INVALID_LOGIN_CREDENTIALS.value


@pytest.mark.django_db
def test_auth_login_successfully():
    User.objects.create_user(email="test@gmail.com", password="password")

    client = APIClient()
    response = client.post(reverse("token_obtain_pair"), {"email": "test@gmail.com", "password": "password"})

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data


# ** Verify Token Tests **
@pytest.mark.django_db
def test_auth_verify_token_successfully():
    User.objects.create_user(email="test@gmail.com", password="password")


    loginClient = APIClient()
    response = loginClient.post(reverse("token_obtain_pair"), {"email": "test@gmail.com", "password": "password"})

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data

    access_token = response.data["access"]

    verifyTokenClient = APIClient()
    response = verifyTokenClient.post(reverse("token_verify"), {"token": access_token})

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_auth_verify_token_failed_invalid_token():
    access_token = "not token"

    verifyTokenClient = APIClient()
    response = verifyTokenClient.post(reverse("token_verify"), {"token": access_token})

    assert response.status_code == AppAuthException.status_code
    assert response.data["error_code"] == AuthErrorCodes.INVALID_TOKEN.name
    assert response.data["error_message"] == AuthErrorCodes.INVALID_TOKEN.value


# ** Verify Token Tests **
@pytest.mark.django_db
def test_auth_verify_token_with_user_info_successfully():
    user = User.objects.create_user(email="test@gmail.com", password="password")

    token = RefreshToken.for_user(user)
    access_token = str(token.access_token)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get(reverse("token_verify_with_user_info"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data["email"] == "test@gmail.com"
    assert response.data["id"] == str(user.id)
    assert response.data["is_admin"] == user.is_staff


@pytest.mark.django_db
def test_auth_verify_token_with_user_info_as_admin_successfully():
    user = User.objects.create_superuser(email="admin@gmail.com", password="password")

    token = RefreshToken.for_user(user)
    access_token = str(token.access_token)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get(reverse("token_verify_with_user_info"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data["email"] == "admin@gmail.com"
    assert response.data["id"] == str(user.id)
    assert response.data["is_admin"] == user.is_staff
    assert response.data["is_admin"]


@pytest.mark.django_db
def test_auth_verify_token_with_user_info_failed():
    access_token = "token"

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get(reverse("token_verify_with_user_info"))

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.data["error_code"] == AuthErrorCodes.INVALID_TOKEN.name
    assert response.data["error_message"] == AuthErrorCodes.INVALID_TOKEN.value 
