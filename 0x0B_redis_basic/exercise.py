#!/usr/bin/env python3
""" Redis exercise """

import redis
import uuid
from typing import Union


class Cache():
    """ Cache class """
    def __init__(self):
        """Class Constructor."""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis db."""
        k = str(uuid.uuid4())
        self._redis.set(k, data)
        # self._redis.bgsave()
        # print(self._redis.get(k))
        return k


if __name__ == "__main__":
    cache = Cache()
    cache.store("hell0")
