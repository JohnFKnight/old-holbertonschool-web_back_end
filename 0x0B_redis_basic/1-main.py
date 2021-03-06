#!/usr/bin/env python3

from exercise import Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    # print(value, fn)
    key = cache.store(value)
    # print("1-main.py before cache.get ", value, fn)
    # print("1-main.py ", cache.get(key, fn=fn))  # == value)
    # print("\n")
    assert cache.get(key, fn=fn) == value
