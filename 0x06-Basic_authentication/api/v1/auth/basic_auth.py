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
