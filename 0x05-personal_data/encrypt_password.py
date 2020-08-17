#!/usr/bin/env python3
import bcrypt


def hash_password(pwd: str) -> bytes:
    """ Create salt-ed, hash-ed pwd
    """

    # salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes(pwd, 'utf-8'), bcrypt.gensalt())
