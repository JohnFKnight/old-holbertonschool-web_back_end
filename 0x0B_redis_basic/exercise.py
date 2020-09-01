#!/usr/bin/env python3

import redis
import uuid


class Cache():
    def __init__(self):
        """Class Constructor."""
        self._redis = redis.Redis()
        self._redis.flushdb

    def storage(data: str) -> str:
        """Store data in redis db."""
        k = str(uid.uuid4())
        self._redis.set({k: data})
        return key
