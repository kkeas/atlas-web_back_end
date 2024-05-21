#!/usr/bin/env Python3
"""encrypt password"""

import bcrypt


def hash_password(password: str) -> bytes:
    """hash a password"""

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validates the provided password matches the hashed password"""

    provided_password = password.encode('utf-8')

    return bcrypt.checkpw(provided_password, hashed_password)
