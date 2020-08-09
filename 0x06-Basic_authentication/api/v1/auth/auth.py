#!/usr/bin/env python3
""" Module of API Authentication views
"""
from flask import request   # , jsonify, abort
# from api.v1.views import app_views

class Auth():

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Public method require_auth
        """
        return False


    def authorization_header(self, request=None) -> str:
        """ Public method auth...header
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ Request current user
        """
        return None
