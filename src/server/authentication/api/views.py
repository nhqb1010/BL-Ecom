from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenVerifySerializer
from rest_framework_simplejwt.exceptions import TokenError

from app.errors.error_codes import AuthErrorCodes
from app.errors.exceptions import AppAuthException
from app.errors.utils import format_error_response


@api_view(['POST'])
def login_view(request):
    serializer = TokenObtainPairSerializer(data=request.data)

    try: 
        serializer.is_valid()
    except AuthenticationFailed:
        error = AppAuthException(AuthErrorCodes.INVALID_LOGIN_CREDENTIALS)
        return Response(format_error_response(error), status=error.status_code)
    
    return Response(serializer.validated_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def verify_token_view(request):
    serializer = TokenVerifySerializer(data=request.data)

    try:
        serializer.is_valid()
    except TokenError as _:
        error = AppAuthException(AuthErrorCodes.INVALID_TOKEN)
        return Response(format_error_response(error), status=error.status_code)

    return Response(serializer.validated_data, status=status.HTTP_200_OK)
