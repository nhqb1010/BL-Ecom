from http import HTTPStatus
from typing import Any

from rest_framework.response import Response


def process_rest_response(
    data: dict[str, Any], status_code: int = HTTPStatus.OK
) -> Response:
    """
    Process the REST response.

    Args:
        data (dict[str, Any]): The data to be included in the response payload.
        status_code (int, optional): The HTTP status code for the response. Defaults to 200 (OK).

    Returns:
        Response: The processed response object.

    """
    response_payload = {"data": data}
    return Response(response_payload, status=status_code)
