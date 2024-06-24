from enum import Enum
from http import HTTPStatus

from app.errors.exceptions import AppException


class AuthErrorCodes(Enum):
    pass


class AppAuthException(AppException):
    """Exception raised for authentication errors in the application.

    Attributes:
        error (AuthErrorCodes): The error code associated with the exception.
    """

    status_code = HTTPStatus.UNAUTHORIZED

    def __init__(self, error: AuthErrorCodes):
        super().__init__(error.value, error.name, self.status_code)


class JwtErrorCodes(AuthErrorCodes):
    """
    Enum class representing JWT errors.
    """

    INVALID_TOKEN = "Access token is invalid."
    EXPIRED_TOKEN = "Access token has expired."
    MISSING_TOKEN = "Access token is missing."


class JwtAuthException(AppAuthException):
    """Exception raised for JWT authentication errors in the application.

    Attributes:
        error (JwtErrorCodes): The error code associated with the exception.
    """

    status_code = HTTPStatus.UNAUTHORIZED

    def __init__(self, error: JwtErrorCodes):
        super().__init__(error)
