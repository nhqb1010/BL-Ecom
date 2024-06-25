import pytest
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from app.auth.constants import AppAuthException, JwtErrorCodes
from authentication.constants.error_codes import AuthErrorCodes


User = get_user_model()


# ** Login Tests **
@pytest.mark.django_db
def test_auth_login_failed_cuz_wrong_password():
    User.objects.create_user(email="test@gmail.com", password="password")

    client = APIClient()
    response = client.post(
        reverse("token_obtain_pair"),
        {"email": "test@gmail.com", "password": "wrong_password"},
    )
    data = response.data["error"]

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert data["error_code"] == AuthErrorCodes.INVALID_LOGIN_CREDENTIALS.name
    assert data["error_message"] == AuthErrorCodes.INVALID_LOGIN_CREDENTIALS.value


@pytest.mark.django_db
def test_auth_login_failed_cuz_wrong_email():
    User.objects.create_user(email="test@gmail.com", password="password")

    client = APIClient()
    response = client.post(
        reverse("token_obtain_pair"),
        {"email": "test1@gmail.com", "password": "password"},
    )
    data = response.data["error"]

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert data["error_code"] == AuthErrorCodes.INVALID_LOGIN_CREDENTIALS.name
    assert data["error_message"] == AuthErrorCodes.INVALID_LOGIN_CREDENTIALS.value


@pytest.mark.django_db
def test_auth_login_successfully():
    User.objects.create_user(email="test@gmail.com", password="password")

    client = APIClient()
    response = client.post(
        reverse("token_obtain_pair"),
        {"email": "test@gmail.com", "password": "password"},
    )

    assert response.status_code == HTTPStatus.OK
    assert "access" in response.data["data"]
    assert "refresh" in response.data["data"]


# ** Verify Token Tests **
@pytest.mark.django_db
def test_auth_verify_token_successfully():
    User.objects.create_user(email="test@gmail.com", password="password")

    loginClient = APIClient()
    response = loginClient.post(
        reverse("token_obtain_pair"),
        {"email": "test@gmail.com", "password": "password"},
    )
    data = response.data["data"]

    assert response.status_code == HTTPStatus.OK
    assert "access" in data

    access_token = data["access"]

    verifyTokenClient = APIClient()
    response = verifyTokenClient.post(reverse("token_verify"), {"token": access_token})

    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_auth_verify_token_failed_invalid_token():
    access_token = "not token"

    verifyTokenClient = APIClient()
    response = verifyTokenClient.post(reverse("token_verify"), {"token": access_token})
    data = response.data["error"]

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert data["error_code"] == AuthErrorCodes.INVALID_TOKEN.name
    assert data["error_message"] == AuthErrorCodes.INVALID_TOKEN.value


@pytest.mark.django_db
def test_auth_verify_token_after_user_deleted():
    user = User.objects.create_superuser(email="admin@gmail.com", password="password")

    token = RefreshToken.for_user(user)
    access_token = str(token.access_token)

    client = APIClient()
    response = client.post(reverse("token_verify"), {"token": access_token})

    assert response.status_code == HTTPStatus.OK

    user.delete()
    assert User.objects.filter(email="admin@gmail.com").first() is None

    client = APIClient()
    response2 = client.post(reverse("token_verify"), {"token": access_token})

    assert response2.status_code == HTTPStatus.OK


# ** Verify Token Tests **
@pytest.mark.django_db
def test_auth_verify_user_access_successfully():
    user = User.objects.create_user(email="test@gmail.com", password="password")

    token = RefreshToken.for_user(user)
    access_token = str(token.access_token)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get(reverse("token_verify_with_user_info"))
    data = response.data["data"]

    assert response.status_code == HTTPStatus.OK
    assert data["email"] == "test@gmail.com"
    assert data["id"] == str(user.id)
    assert data["is_admin"] == user.is_staff


@pytest.mark.django_db
def test_auth_verify_user_access_as_admin_successfully():
    user = User.objects.create_superuser(email="admin@gmail.com", password="password")

    token = RefreshToken.for_user(user)
    access_token = str(token.access_token)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get(reverse("token_verify_with_user_info"))
    data = response.data["data"]

    assert response.status_code == HTTPStatus.OK
    assert data["email"] == "admin@gmail.com"
    assert data["id"] == str(user.id)
    assert data["is_admin"] == user.is_staff
    assert data["is_admin"]


@pytest.mark.django_db
def test_auth_verify_user_access_failed():
    access_token = "token"

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get(reverse("token_verify_with_user_info"))
    data = response.data["error"]

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert data["error_code"] == JwtErrorCodes.INVALID_TOKEN.name
    assert data["error_message"] == JwtErrorCodes.INVALID_TOKEN.value


@pytest.mark.django_db
def test_auth_verify_user_access_failed_after_user_deleted():
    user = User.objects.create_superuser(email="admin@gmail.com", password="password")

    token = RefreshToken.for_user(user)
    access_token = str(token.access_token)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get(reverse("token_verify_with_user_info"))
    data = response.data["data"]

    assert response.status_code == HTTPStatus.OK
    assert data["email"] == "admin@gmail.com"
    assert data["id"] == str(user.id)
    assert data["is_admin"] == user.is_staff

    user.delete()
    assert User.objects.filter(email="admin@gmail.com").first() is None

    response2 = client.get(reverse("token_verify_with_user_info"))
    data2 = response2.data["error"]

    assert response2.status_code == AppAuthException.status_code
    assert data2["error_code"] == JwtErrorCodes.INVALID_TOKEN.name
    assert data2["error_message"] == JwtErrorCodes.INVALID_TOKEN.value
