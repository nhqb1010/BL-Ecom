from django.contrib.auth import get_user_model
import pytest

from account.models import User as CustomUser

User = get_user_model()

# *** Custom User tests ***
@pytest.mark.django_db
def test_custom_user_model_using_get_user_model():
    user = User.objects.create_user(email="test@gmail.com", password="password")
    assert user.email == "test@gmail.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


@pytest.mark.django_db
def test_create_superuser_using_get_user_model():
    admin_user = User.objects.create_superuser(email="admin@gmail.com", password="password")
    assert admin_user.email == "admin@gmail.com"
    assert admin_user.is_active
    assert admin_user.is_staff
    assert admin_user.is_superuser


@pytest.mark.django_db
def test_custom_user_model_from_direct_import():
    user = CustomUser.objects.create_user(email="test@gmail.com", password="password")
    assert user.email == "test@gmail.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


@pytest.mark.django_db
def test_create_superuser_from_direct_import():
    admin_user = CustomUser.objects.create_superuser(email="admin@gmail.com", password="password")
    assert admin_user.email == "admin@gmail.com"
    assert admin_user.is_active
    assert admin_user.is_staff
    assert admin_user.is_superuser