#!/usr/bin/env python3
""" Auth class
"""

import uuid
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

    def valid_login(self, email: str, password: str) -> bool:
        """ Validate login
        """
        try:
            usr = self._db.find_user_by(email=email)
            hpwd = usr.hashed_password
            if bcrypt.checkpw(password.encode(), hpwd):
                return True
            else:
                return False
        except Exception as e:
            return False

    def create_session(self, email: str) -> str:
        """ Create and set user session id.
        """
        try:
            usr = self._db.find_user_by(email=email)
            sess = _generate_uuid()
            self._db.update_user(usr.id, session_id=sess)
            return sess
            # self._db.update_user(usr.id, session_id=_generate_uuid())
            # return usr.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """ Find user from session id.
        """
        try:
            usr = self._db.find_user_by(session_id=session_id)
            return usr
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        try:
            usr = self._db.find_user_by(id=user_id)
            self._db.update_user(usr.id, 'usr.id=None')
            print(usr.id, usr.email)
            return None
        except NoResultFound:
            return None


def _hash_password(password: str) -> str:
    """ Create salt-ed, hash-ed pwd
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Return uuid string.
    """

    return str(uuid.uuid4())
