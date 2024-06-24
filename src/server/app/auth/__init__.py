from django.http import HttpRequest
from rest_framework import authentication

from app.auth.jwt_manager import get_user_from_jwt_request


class JwtAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request: HttpRequest):
        user = get_user_from_jwt_request(request)

        if user is None:
            return None

        return (user, None)
