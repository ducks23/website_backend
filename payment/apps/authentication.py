import jwt
import os
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User


class TokenAuth(BaseAuthentication):
    def authenticate(self, request):
        """
        Authenticate jwt token with stored secret.
        """
        token = request.headers.get("Authorization")
        contents = jwt.decode(
            token, os.environ.get("TOKEN_SECRET"), algorithms=["HS256"]
        )
        try:
            user = User.objects.get(username=contents["user"])
        except User.DoesNotExist:
            raise AuthenticationFailed()

        return (user, None)
