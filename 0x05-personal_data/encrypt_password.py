#!/usr/bin/env python3
""" Hash a password
"""

import bcrypt


def hash_password(pwd: str) -> bytes:
    """ Create salt-ed, hash-ed pwd
    """

    return bcrypt.hashpw(bytes(pwd, 'utf-8'), bcrypt.gensalt())


def is_valid(hpwd: bytes, pwd: str) -> bool:
    """ Check valid password
    """

    if bcrypt.checkpw(pwd.encode(), hpwd):
        return True
    else:
        return False
