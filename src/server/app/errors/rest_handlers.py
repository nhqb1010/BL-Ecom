from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed

from app.errors.error_codes import AuthErrorCodes
from app.errors.exceptions import AppAuthException


def app_exception_handler(exc, context):
    """
    Custom exception handler for django rest framework for the application.

    Args:
        exc (Exception): The exception that was raised.
        context (dict): The context in which the exception was raised.

    Returns:
        Response: The response object to be returned.

    """

    response = exception_handler(exc, context)

    # Handle authentication errors
    if isinstance(exc, AuthenticationFailed):
        auth_message = exc.detail

        is_auth_error = auth_message in AuthErrorCodes.__members__

        if is_auth_error:
            error = AppAuthException(AuthErrorCodes[auth_message])
            response.data = error.to_dict()
            response.status_code = error.status_code

    return response
