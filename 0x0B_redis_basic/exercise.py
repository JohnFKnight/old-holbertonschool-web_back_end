#!/usr/bin/env python3
""" Redis exercise """

import redis
import uuid


class Cache():
    """ Cache class """
    def __init__(self):
        """Class Constructor."""
        self_redis = redis.Redis()
        self._redis.flushdb

    def storage(data: str) -> str:
        """Store data in redis db."""
        k = str(uid.uuid4())
        self._redis.set({k: data})
        # self._redis.bgsave()
        return k
