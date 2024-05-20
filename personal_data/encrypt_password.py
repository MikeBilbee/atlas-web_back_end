#!/usr/bin/env python3
"""
A hash_password function that expects one string
argument name password and returns a salted, hashed
password, which is a byte string.

Use the bcrypt package to perform the hashing (with hashpw).
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes your passwords"""

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
