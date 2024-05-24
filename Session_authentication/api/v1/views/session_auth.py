#!/usr/bin/env python3
"""View route for session auth"""

from flask import Blueprint
from api.v1.views import app_views
from flask import jsonify, request, make_response
import os
from models.user import User

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


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
