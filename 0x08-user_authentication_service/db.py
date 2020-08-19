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

    def find_user_by(self, **keyword):
        self.keyword = keyword
        session = self._session
        try:
            return session.query(User).filter_by(**self.keyword).first()
        except NoResultFound as e:
            # print("no result err" , e)
            raise e
        except InvalidRequestError as e:
            # print("invalid req err ", e)
            raise e
        # finally:
        #     raise NoResultFound()
        # return res
