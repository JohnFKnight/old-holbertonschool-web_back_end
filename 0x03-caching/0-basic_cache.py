#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        self.cache_data = {}

    def put(self, key, item):
        if (key is None or item is None):
            pass
        self.cache_data[key] = item

    def get(self, key):
        if (key is None or not key):
            pass
        return self.cache_data.get(key)
