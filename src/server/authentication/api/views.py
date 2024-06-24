from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenVerifySerializer,
)
from rest_framework_simplejwt.exceptions import TokenError

from app.auth.constants import AppAuthException
from app.errors.error_codes import AuthErrorCodes
from app.errors.utils import format_error_response
from account.serializers import UserSerializer

User = get_user_model()


@api_view(["POST"])
def login_view(request):
    serializer = TokenObtainPairSerializer(data=request.data)

    try:
        serializer.is_valid()
    except AuthenticationFailed:
        error = AppAuthException(AuthErrorCodes.INVALID_LOGIN_CREDENTIALS)
        return Response(format_error_response(error), status=error.status_code)

    return Response(serializer.validated_data, status=status.HTTP_200_OK)


@api_view(["POST"])
def verify_token_view(request):
    serializer = TokenVerifySerializer(data=request.data)

    try:
        serializer.is_valid()
    except TokenError as _:
        error = AppAuthException(AuthErrorCodes.INVALID_TOKEN)
        return Response(
            format_error_response(error), status=status.HTTP_400_BAD_REQUEST
        )

    return Response({}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def verify_token_with_user_info_view(request):
    email = request.user.email
    user = get_object_or_404(User, email=email)

    return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
