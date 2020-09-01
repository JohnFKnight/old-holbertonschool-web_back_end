#!/usr/bin/env python3

import redis
import uuid


class Cache():
    def __init__(self):
        """Class Constructor."""
        self._redis = redis()
        self._redis.flushdb

    def storage(data: str) -> str:
        """Store data in redis db."""
        key = str(uid.uuid4())
        self._redis[key] = data
        return key
