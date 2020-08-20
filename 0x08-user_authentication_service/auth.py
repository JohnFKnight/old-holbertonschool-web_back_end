#!/usr/bin/env python3
""" Auth class
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Constructor
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError('User ' + email + ' already exists')
        except NoResultFound:
            hpwd = _hash_password(password)
            return self._db.add_user(email, hpwd)


def _hash_password(password: str) -> str:
    """ Create salt-ed, hash-ed pwd
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())