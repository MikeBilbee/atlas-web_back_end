#!/usr/bin/env python3
"""
WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
"""

from api.v1.views import app_views
from api.v1.auth.auth import Auth
from models.user import User
import uuid
from flask import jsonify, request, abort, make_response
from models.user import User
import os


class SessionAuth(Auth):
    """Session Athentication class, inheriting from Auth"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates session ID"""

        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        SessionAuth.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns User ID based on session ID"""

        if session_id is None or not isinstance(session_id, str):
            return None

        user_id = SessionAuth.user_id_by_session_id.get(session_id)

        return user_id

    def session_cookie(self, request=None):
        """Returns Cookie value"""

    def current_user(self, request=None):
        """returns User instance based on cookie value"""
        cookie_value = self.session_cookie(request)
        if cookie_value is None:
            return None
        user = self.user_id_for_session_id(cookie_value)
        return User.get(user)

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handles user login using session authentication."""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    user_list = User.search(email=email)
    if not user_list:
        return jsonify({"error": "no user found for this email"}), 404

    user = user_list[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(user.id)
    response = make_response(jsonify(user.to_dict()))
    response.set_cookie(
        os.getenv('SESSION_NAME'), session_id
    )
    return response, 200
