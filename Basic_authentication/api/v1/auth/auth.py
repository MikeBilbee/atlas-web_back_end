#!/usr/bin/env python3
"""
Authorization for the API server
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Authorizations Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks for required authorization"""

        return False

    def authorization_header(self, request=None) -> str:
        """Retrieves auth header"""

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets current user"""

        return None
