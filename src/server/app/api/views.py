from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def health_check(_: HttpRequest):
    """
    Endpoint for performing a health check.

    Args:
        _: The HttpRequest object (unused).

    Returns:
        A Response object with a JSON payload containing the status "ok" and HTTP status code 200.
    """
    return Response({"status": "ok"}, status=status.HTTP_200_OK)
