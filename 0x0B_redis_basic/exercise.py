#!/usr/bin/env python3
""" Redis exercise """

import redis
from  uuid import uuid4
from typing import Union, Callable, List


class Cache():
    """ Cache class """
    def __init__(self):
        """Class Constructor."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis db."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> str:
        """Store data in redis db."""
        k = self.store(key)
        return (self._redis.get(k).decode('utf-8'))

    def get_str():
        """Store data in redis db."""
        pass

    def get_int():
        """Store data in redis db."""
        pass

# if __name__ == "__main__":
#     cache = Cache()
#     print(cache.store("hell0"))
