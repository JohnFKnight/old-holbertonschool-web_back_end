#!/usr/bin/env python3

import bcrypt


def _hash_password(password: str) -> str:
    """ Create salt-ed, hash-ed pwd
    """

    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
