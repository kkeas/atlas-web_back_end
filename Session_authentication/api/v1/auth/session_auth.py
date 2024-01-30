#!/usr/bin/env Python3

"""session authorization class"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """validate if everything inherits correctly without any overloading
        validate the “switch” by using environment variables"""
    pass
