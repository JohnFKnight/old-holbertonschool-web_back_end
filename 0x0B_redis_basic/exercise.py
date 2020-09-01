#!/usr/bin/env python3

import redis
import uuid

class Cache():
    def __init__(self):
        """Class Constructor."""
        self._redis = redis()
        self._redis.flushdb

    def storage(data: str) -> str:
        key = str(uid.uuid4())
        data.set(key)
        return key
