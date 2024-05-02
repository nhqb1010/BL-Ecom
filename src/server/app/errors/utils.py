from typing import Any

from .exceptions import AppException


def format_error_response(error: AppException, detail: str = None) -> dict[str, Any]:
    return error.toDict() if not detail else error.toDict() | {'error_detail': detail}