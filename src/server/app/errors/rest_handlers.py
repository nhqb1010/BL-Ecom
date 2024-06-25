from rest_framework.views import exception_handler
from rest_framework.response import Response

from app.errors.exceptions import AppException


def app_exception_handler(exc, context):
    """
    Custom exception handler for django rest framework for the application.

    Args:
        exc (Exception): The exception that was raised.
        context (dict): The context in which the exception was raised.

    Returns:
        Response: The response object to be returned.

    """

    # Handle app error
    if isinstance(exc, AppException):
        response_data = {
            "error": exc.to_dict(),
        }
        return Response(response_data, status=exc.status_code)

    return exception_handler(exc, context)
