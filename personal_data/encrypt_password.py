#!/usr/bin/env Python3
"""encrypt password"""

import bycrypt

def hash_password(password: str) -> bytes:
    """hash a password"""

    hashed = bycrypt.hashpw(password.encode('utf-8'), bycrypt.gensalt())
    return hashed
