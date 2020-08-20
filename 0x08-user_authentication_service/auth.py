#!/usr/bin/env python3

import bcrypt

from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Constructor
        """
        self._db = DB()

    def _hash_password(self, password: str) -> str:
        """ Create salt-ed, hash-ed pwd
        """
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """ Register user
        """
        self.email = email
        try:
            self._db.find_user_by(email=self.email)
            print("FOUND USER", email)
            raise ValueError('User ' + email + ' already exists')
        except Exception:
            print("USER NOT FOUND", email)
            self._hash_password(password)
            # session = self._db._session()
            return self._db.add_user(email, self._hash_password(password))
