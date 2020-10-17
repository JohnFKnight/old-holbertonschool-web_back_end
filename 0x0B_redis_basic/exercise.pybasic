#!/usr/bin/env python3
""" Redis exercise """

import redis
import uuid
from typing import Union, Callable, List


class Cache():
    """ Cache class """
    def __init__(self):
        """Class Constructor."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis db."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
