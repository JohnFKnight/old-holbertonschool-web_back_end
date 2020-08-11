#!/usr/bin/env python3
""" Module of API Authentication views
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import re
import base64


class BasicAuth(Auth):
    """ Basic Auth class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Base 64 auth header
        """

        if ((authorization_header is None)
                or (not isinstance(authorization_header, str)) or
                (re.search("^Basic ", str(authorization_header)) is None)):
            return None
        else:
            try:
                return re.search("(?<=Basic ).*",
                                 str(authorization_header)).group()
            except Exception:
                return re.search("(?<=Basic ).*",  str(authorization_header))

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Base 64 decode auth header
        """
        bah = base64_authorization_header

        if ((base64_authorization_header is None)
                or (not isinstance(base64_authorization_header, str))):
            return None
        try:
            bah1 = bah.encode("UTF-8")
            bah2 = base64.b64decode(bah1)
            bah3 = bah2.decode("UTF-8")
            return bah3
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Base 64 decode auth header
        """
        dbah = decoded_base64_authorization_header

        if (dbah is None) or (not isinstance(dbah, str)) or (":" not in dbah):
            return (None, None)
        res = dbah.split(":")
        return tuple(res)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Basic User
        """
        from models.user import User

        user = User()

        if ((user_email is None or not isinstance(user_email, str)
                 or (user_pwd is None or not isinstance(user_pwd, str)):
             return None
        
