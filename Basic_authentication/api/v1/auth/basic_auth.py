#!/usr/bin/env Python3

"""Basic Auth class file"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """basic auth class"""
    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """authorization header for basic authentication"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]
