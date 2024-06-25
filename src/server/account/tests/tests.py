from django.contrib.auth import get_user_model
import pytest

from account.models import User as CustomUser
from account.services import user as user_sv

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
    admin_user = User.objects.create_superuser(
        email="admin@gmail.com", password="password"
    )
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
    admin_user = CustomUser.objects.create_superuser(
        email="admin@gmail.com", password="password"
    )
    assert admin_user.email == "admin@gmail.com"
    assert admin_user.is_active
    assert admin_user.is_staff
    assert admin_user.is_superuser


# *** User services tests ***
@pytest.mark.django_db
def test_user_services_find_user():
    user = CustomUser.objects.create_superuser(
        email="admin@gmail.com", password="password"
    )

    _user = user_sv.find_user(email="admin@gmail.com")
    assert _user.email == user.email
    assert _user.is_active == user.is_active
    assert _user.id == user.id

    _user2 = user_sv.find_user(id=user.id)
    assert _user2.id == user.id
    assert _user2.email == user.email
    assert _user2.is_active == user.is_active


@pytest.mark.django_db
def test_user_services_find_user_not_exist():
    user = user_sv.find_user(email="admin@gmail.com")
    assert user is None

    user2 = user_sv.find_user(id=1)
    assert user2 is None


@pytest.mark.django_db
def test_user_services_get_user_by_email():
    user = CustomUser.objects.create_superuser(
        email="admin@gmail.com", password="password"
    )

    _user = user_sv.get_user_by_email(email="admin@gmail.com")
    assert _user.email == user.email
    assert _user.is_active == user.is_active
    assert _user.id == user.id


@pytest.mark.django_db
def test_user_services_get_user_by_email_not_exist():
    should_error = False

    try:
        user_sv.get_user_by_email(email="admin@gmail.com")
    except Exception as e:
        should_error = True
        assert type(e) == CustomUser.DoesNotExist

    assert should_error
