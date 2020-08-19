from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from user import Base
from user import User


class DB:

    def __init__(self):
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User():
        """ Add user. Create session,
        then add user(email, pwd)?
        """
        self.email = email
        self.hpwd = hashed_password
        session = self._session
        try:
            row = User(email=self.email,
                       hashed_password=self.hpwd)
            session.add(row)
            session.commit()
        except SQLAlchemyError as e:
            print(e)
        finally:
            session.close()

        added_user = session.query(User).first()
        return added_user
