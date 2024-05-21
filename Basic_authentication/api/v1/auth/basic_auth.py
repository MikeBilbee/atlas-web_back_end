#!/usr/bin/env python3
"""
Basic Authorization for the API server
"""

from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar


class BasicAuth(Auth):
    """Basic Authorizations Class, Inheriting from Auth"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:  # noqa E501
        """Gets the Base64 section of the Auth Header"""

        if authorization_header is None or not isinstance(authorization_header, str):  # noqa E501
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]


    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Returns the decoded value of a Base64 string"""

        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except base64.binascii.Error:
            return None
