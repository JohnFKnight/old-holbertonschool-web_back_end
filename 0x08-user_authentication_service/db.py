#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError, SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound

from user import Base
from user import User
from typing import TypeVar, Generic


class DB:
    """ Class DB
    """
    def __init__(self):
        """ Class constructor.
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
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
        """ Add user. Create session,
        then add user(email, pwd)?
        """
        self.email = email
        self.hpwd = hashed_password
        session = self._session
        row = User(email=self.email,
                   hashed_password=self.hpwd)
        session.add(row)
        session.commit()
        return row

        # added_user = session.query(User).first()

    def find_user_by(self, **keyword) -> User:
        """ Find user based on keyword (key=value)
        """
        self.keyword = keyword
        session = self._session
        # for k, v in self.keyword.items():
        # key = getattr(User, k)
        try:
            res = session.query(User).filter_by(**self.keyword).first()
            if not res:
                raise NoResultFound
        except NoResultFound as e:
            raise e
        except InvalidRequestError as e:
            raise e
        return res

    def update_user(self, user_id: int, **keyword) -> None:
        """ Update user attributes.
        """
        session = self._session
        self.uid = user_id
        self.kwd = keyword
        user = self.find_user_by(id=self.uid)
        for k, v in self.kwd.items():
            try:
                getattr(user, k)
                setattr(user, k, v)
            except Exception:
                raise ValueError
        session.commit()
        return None