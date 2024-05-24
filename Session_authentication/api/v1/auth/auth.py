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

        if not path or not excluded_paths:
            return True

        return path.rstrip('/') not in {p.rstrip('/') for p in excluded_paths}

    def authorization_header(self, request=None) -> str:
        """Retrieves auth header"""

        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets current user"""

        return None
