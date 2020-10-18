#!/usr/bin/env python3
""" Redis exercise """

import redis
import uuid
from typing import Union, Callable, List, Optional


class Cache():
    """ Cache class """
    def __init__(self):
        """Class Constructor."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis db."""
        k = str(uuid.uuid4())
        self._redis.set(k, data)
        return k

    def get(self, key: str, fn: Optional[Callable]) -> str:
        """Get data from redis db."""
        k = self._redis.get(key)
        if fn:
            return fn(k)
        return k

    def get_str():
        """Get string from redis db."""
        pass

    def get_int():
        """Get int from  redis db."""
        pass

# if __name__ == "__main__":
#     cache = Cache()
#     print(cache.store("hell0"))
