from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(LoginSerializer, self).validate(attrs)

        return data
