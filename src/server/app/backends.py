from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from authentication.jwt import jwt_authenticate_from_request

User = get_user_model()


class JwtAuthenticationBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        print("fking backend", request)
        if request is None:
            return None

        data = jwt_authenticate_from_request(request)
        print(data)
        
        return jwt_authenticate_from_request(request)
    
    def get_user(self, identifier):
        print("fking backend get_user", identifier)
        try:
            return User.objects.get(email=identifier, is_active=True)
        except User.DoesNotExist:
            return None
        