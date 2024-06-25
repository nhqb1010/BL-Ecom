from typing import Any, Optional

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from account.models import User as UserType


User = get_user_model()


def find_user(**kwargs: dict[str, Any]) -> Optional[UserType]:
    """
    Find a user based on the provided keyword arguments.
    Returns None if the user does not exist.

    Args:
        **kwargs: Keyword arguments used to filter the user.

    Returns:
        UserType: The found user object if it exists, otherwise None.
    """
    try:
        user = User.objects.get(**kwargs)
        return user
    except ObjectDoesNotExist as _:
        return None


def get_user_by_email(email: str) -> UserType:
    """
    Retrieve a user by their email address.
    Raises a DoesNotExist exception if the user does not exist.

    Args:
        email (str): The email address of the user.

    Returns:
        User: The user object matching the provided email address.
    """
    return User.objects.get(email=email)
