#!/usr/bin/env python3
""" DB class to Add, find, update users
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError, SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound

from user import Base
from user import User
from typing import TypeVar, Generic
import bcrypt


class DB:
    """ Class DB for users
    """
    def __init__(self):
        """ Class constructor.
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        # Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ Create session.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add user. Create session, then add user(email, pwd)?
        """
        hpwd = hashed_password
        session = self._session
        row = User(email=email,
                   hashed_password=hpwd)
        session.add(row)
        session.commit()
        return row

        # added_user = session.query(User).first()

    def find_user_by(self, **keyword) -> User:
        """ Find user based on keyword (key=value)
        """
        session = self._session
        # for k, v in self.keyword.items():
        # key = getattr(User, k)
        try:
            res = session.query(User).filter_by(**keyword).first()
            if not res:
                raise NoResultFound
        # except NoResultFound as e:
        #     raise e
        except InvalidRequestError as e:
            raise e
        return res

    def update_user(self, user_id: int, **keyword) -> None:
        """ Update user attributes with keyword.
        """
        session = self._session
        uid = user_id
        kwd = keyword
        user = self.find_user_by(id=uid)
        try:
            for k, v in kwd.items():
                getattr(user, k)
                setattr(user, k, v)
        except Exception:
            raise ValueError
        session.commit()
        return None
