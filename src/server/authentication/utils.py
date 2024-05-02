from django.http import HttpRequest


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
    
    return auth_header.split(" ")[1] if "Bearer" in auth_header else None
