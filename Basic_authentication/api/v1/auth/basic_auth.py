#!/usr/bin/env python3
"""
Basic Authorization for the API server
"""

from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic Authorizations Class, Inheriting from Auth"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:  # noqa E501
        """Gets the Base64 section of the Auth Header"""

        if authorization_header is None or not isinstance(authorization_header, str):  # noqa E501
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:  # noqa E501
        """Returns the decoded value of a Base64 string"""

        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):  # noqa E501
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except base64.binascii.Error:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> Tuple[str, str]:  # noqa E501
        """returns the user email and password from the Base64 decoded value"""

        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_email, user_password = decoded_base64_authorization_header.split(':', 1)  # noqa E501
        return user_email, user_password

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Creates User instance based on his email and password."""

        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None
