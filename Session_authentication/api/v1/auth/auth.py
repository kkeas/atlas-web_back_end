#!/usr/bin/env Python3

""" this is a comment """

from flask import request
from typing import List, TypeVar
import os


class Auth:
    """class to manage API authorization"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method to require authorization"""

        if path is None:
            return True

        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        for p in excluded_paths:
            standardized_p = p.rstrip('/')
            if standardized_p in path or p.startswith(path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns auth header"""
        if request is None:
            return None

        if 'Authorization' not in request.headers:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """returns current user"""
        return None

    def session_cookie(self, request=None):
        """Retrieves the value of the session cookie from the request."""
        if request is None:
            return None
        return request.cookies.get(os.getenv("SESSION_NAME"))
