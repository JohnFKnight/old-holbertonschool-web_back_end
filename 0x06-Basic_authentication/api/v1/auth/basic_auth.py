#!/usr/bin/env python3
""" Module of API Authentication views
"""
from flask import request   # , jsonify, abort
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Auth class
    """
    pass
