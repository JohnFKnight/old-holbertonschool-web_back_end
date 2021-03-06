#!/usr/bin/env python3
""" Create User model with SQLAlchemy
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """User subclass of Base"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    email = Column(String(250), nullable=True)
    hashed_password = Column(String(250), nullable=True)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
