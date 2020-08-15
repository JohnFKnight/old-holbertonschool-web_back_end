#!/usr/bin/env python3
""" Module of API Authentication views
"""
from flask import request   # , jsonify, abort
from typing import List, TypeVar
import re
# from api.v1.views import app_views


class Auth():
    """ Autho class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Public method require_auth
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        for excluded in excluded_paths:
            wildcard = excluded.find("*")
            if wildcard >= 0:
                if excluded.paths[:wildcard] in path:
                    return False
        if path[-1] != "/":
            path += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Public method auth...header
        """
        if request is None:
            return None
        if 'Authorization' in request.headers:
            return request.headers['Authorization']
        else:
            return None

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Request current user
        """
        return None
