#!/usr/bin/env python3
""" Module of API Authentication views
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import re


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
            # print("IN THE ELSE")
            try:
                return re.search("(?<=Basic ).*",
                                 str(authorization_header)).group()
            except Exception:
                return re.search("(?<=Basic ).*",  str(authorization_header))
