from http import HTTPStatus

from django.http import HttpRequest
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenVerifySerializer,
)
from rest_framework_simplejwt.exceptions import TokenError

from app.auth.constants import AppException
from app.api.utils import process_rest_response
from account.serializers import UserSerializer
from authentication.constants.error_codes import AuthErrorCodes

User = get_user_model()


@api_view(["POST"])
def login_view(request: HttpRequest):
    serializer = TokenObtainPairSerializer(data=request.data)

    try:
        serializer.is_valid()
    except AuthenticationFailed:
        raise AppException(
            AuthErrorCodes.INVALID_LOGIN_CREDENTIALS,
            status_code=HTTPStatus.BAD_REQUEST,
        )

    return process_rest_response(serializer.validated_data)


@api_view(["POST"])
def verify_token_view(request: HttpRequest):
    serializer = TokenVerifySerializer(data=request.data)

    try:
        serializer.is_valid()
    except TokenError as _:
        raise AppException(
            AuthErrorCodes.INVALID_TOKEN, status_code=HTTPStatus.BAD_REQUEST
        )

    return process_rest_response(serializer.validated_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def verify_token_with_user_info_view(request: HttpRequest):
    email = request.user.email
    user = get_object_or_404(User, email=email)

    return process_rest_response(UserSerializer(user).data)
