#!/usr/bin/env python3
"""
Basic Authorization for the API server
"""

from api.v1.auth.auth import Auth, TypeVar


class BasicAuth(Auth):
    """Basic Authorizations Class, Inheriting from Auth"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Gets the Base64 section of the Auth Header"""

        if authorization_header is None or not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]
