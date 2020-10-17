#!/usr/bin/env python3
""" Redis exercise """

import redis
from uuid import uuid4
from typing import Union, Callable, List


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
