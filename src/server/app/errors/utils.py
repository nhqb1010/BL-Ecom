from typing import Any

from .exceptions import AppException


def format_error_response(error: AppException, detail: str = None) -> dict[str, Any]:
    """
    Formats an error response based on the given error and optional detail.

    Args:
        error (AppException): The error object to format the response for.
        detail (str, optional): Additional detail to include in the response. Defaults to None.

    Returns:
        dict[str, Any]: The formatted error response as a dictionary.
    """
    return error.to_dict() if not detail else error.to_dict() | {'error_detail': detail}
