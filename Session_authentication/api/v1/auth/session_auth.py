#!/usr/bin/env Python3

"""session authorization class"""

from api.v1.auth.auth import Auth
import uuid
from api.v1.app import app_views
from flask import request, jsonify
from models.user import User

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """new Flask view that handles all routes for the Session authentication"""
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == '':
        jsonify({"error": "email missing"}), 400
    
    if password is None or password == '':
        jsonify({"error": "password missing"}), 400
       
    users = User.search({'email': email})
    if not users:
        jsonify({"error": "no user found for this email"}), 404
    if not User.is_valid_password(password):
        jsonify({"error": "wrong password"}), 401

    session_id = Auth.create_session(User.id)
    response = jsonify(User.to_json())
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)
    
    return response


class SessionAuth(Auth):
    """validate if everything inherits correctly without any overloading
        validate the “switch” by using environment variables"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create a session"""

        if user_id is None:
            return None

        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns a cookie value from a request """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)
