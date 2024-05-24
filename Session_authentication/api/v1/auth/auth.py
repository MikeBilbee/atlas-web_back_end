#!/usr/bin/env python3
"""
Authorization for the API server
"""

from flask import request
from typing import List, TypeVar
import os


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
    
    def session_cookie(self, request=None):
        if request is None:
            return None

        session_name = os.environ.get('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name)
