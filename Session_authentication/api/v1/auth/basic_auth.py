#!/usr/bin/env Python3

"""Basic Auth class file"""

from api.v1.auth.auth import Auth
from models.user import User
from typing import List, TypeVar
import base64


class BasicAuth(Auth):
    """basic auth class"""
    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """authorization header for basic authentication"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
          self, base64_authorization_header: str
          ) -> str:
        """decode a Base64 string"""
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            decoded_bytes = base64.b64decode(base64_bytes)
            decoded_utf8 = decoded_bytes.decode('utf-8')
            return decoded_utf8

        except (ValueError, TypeError, base64.binascii.Error):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """returns the user email and password from the Base64 decoded value"""

        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(":")
        return credentials[0], credentials[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        """ returns the User instance based on his email and password """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})

        if not users:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieves the User instance for a request """

        auth_header = self.authorization_header(request)
        if not auth_header:
            return None

        base64_auth = self.extract_base64_authorization_header(auth_header)
        if not base64_auth:
            return None

        decoded = self.decode_base64_authorization_header(base64_auth)
        if not decoded:
            return None

        email, pwd = self.extract_user_credentials(decoded)
        if not email or not pwd:
            return None

        return self.user_object_from_credentials(email, pwd)
