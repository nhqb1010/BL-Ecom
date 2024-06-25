import jwt
from typing import Optional

from django.http import HttpRequest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser

from app.auth.constants import JwtErrorCodes, JwtAuthException

JWT_SECRET_KEY = settings.SECRET_KEY
JWT_HASH_ALGORITHM = settings.__getattr__("SIMPLE_JWT")["ALGORITHM"] or "HS256"

User = get_user_model()


def get_token_from_request(request: HttpRequest) -> str | None:
    """
    Extracts the token from the Authorization header of the given request.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        str | None: The extracted token if it exists, otherwise None.
    """

    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None

    if len(auth_header.split(" ")) != 2:
        return None

    return auth_header.split(" ")[1] if "Bearer" in auth_header else None


def raise_jwt_exception(error: jwt.PyJWTError) -> JwtAuthException:
    if isinstance(error, jwt.ExpiredSignatureError):
        raise JwtAuthException(JwtErrorCodes.EXPIRED_TOKEN)
    elif isinstance(error, jwt.DecodeError):
        raise JwtAuthException(JwtErrorCodes.INVALID_TOKEN)
    else:
        raise JwtAuthException(JwtErrorCodes.INVALID_TOKEN)


def decode_jwt_token(token: str) -> dict:
    """
    Decodes the given JWT token.

    Args:
        token (str): The JWT token to decode.

    Returns:
        dict: The decoded payload of the token.

    Raises:
        JwtAuthException: If the token is invalid or expired.
    """

    try:
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_HASH_ALGORITHM])
    except jwt.PyJWTError as e:
        raise_jwt_exception(e)


def get_user_from_jwt_request(request: HttpRequest) -> Optional[AbstractBaseUser]:
    """
    Retrieves the user associated with the JWT token in the given request.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        Optional[AbstractBaseUser]: The user associated with the JWT token, or None if the token is invalid or no user is found.
    """

    token = get_token_from_request(request)

    if not token:
        return None

    payload = decode_jwt_token(token)

    user_id: str = payload.get("user_id")
    user = User.objects.filter(id=user_id).first()

    if not user:
        raise_jwt_exception(JwtErrorCodes.INVALID_TOKEN)

    return user
