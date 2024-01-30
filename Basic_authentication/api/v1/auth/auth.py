#!/usr/bin/env Python3

""" this is a comment """

from flask import request
from typing import List, TypeVar


class Auth:
    """class to manage API authorization"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method to require authorization"""
        return False

    def authorization_header(self, request=None) -> str:
        """returns auth header"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """returns current user"""
        return None
