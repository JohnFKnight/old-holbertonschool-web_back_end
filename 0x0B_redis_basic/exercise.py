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
        if data is not None:
            k = str(uuid.uuid4())
            self._redis.mset({k: data})
            # self._redis.bgsave()
            print(type(self._redis.get(k).decode('utf-8')))  # == data)
            return k
        else:
            return None

    def get(self, key: str, fn: Callable = None) -> str:
        k = self.store(key)
        # print(self._redis.get(k))
        # print(self._redis.get(k).decode('utf-8'))
        return (self._redis.get(k).decode('utf-8'))

    def get_str():
        pass

    def get_int():
        pass


if __name__ == "__main__":
    cache = Cache()
    print(cache.store("hell0"))
