#!/usr/bin/env Python3
"""encrypt password"""

import bcrypt


def hash_password(password: str) -> bytes:
    """hash a password"""

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
