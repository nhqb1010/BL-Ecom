import jwt
from django.http import HttpRequest
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from app.errors.error_codes import AuthErrorCodes
from .utils import get_token_from_request


User = get_user_model()
JWT_HASH_ALGORITHM = settings.__getattr__("SIMPLE_JWT")["ALGORITHM"] or "HS256"


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request: HttpRequest):
        token = get_token_from_request(request)

        if not token:
            return None

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[JWT_HASH_ALGORITHM])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed(AuthErrorCodes.INVALID_TOKEN.name)
        except jwt.DecodeError:
            raise AuthenticationFailed(AuthErrorCodes.INVALID_TOKEN.name)
        
        # ! Should enhance?
        try:
            user = User.objects.get(id=payload["user_id"])
            return (user, None)
        except User.DoesNotExist:
            raise AuthenticationFailed(AuthErrorCodes.INVALID_TOKEN.name)
        