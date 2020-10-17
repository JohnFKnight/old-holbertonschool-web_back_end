#!/usr/bin/env python3
""" Module for Redis db """
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from sys import byteorder
from functools import wraps


class Cache:
    """ Class for methods that operate a caching system """

    def __init__(self):
        """ Instance of Redis db """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Creates key and stores it with data """
        # uuid must be type cast to str for Redis to be able to accept it
        key = str(uuid4())
        # use pipelining for multi sets, mset() is not approrpiate for a cache
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """ Returns data converted to desired format """
        # default Redis.get in case key does not exist
        data = self._redis.get(key)
        # use callable if one provided
        if fn:
            data = fn(data)
        return data
