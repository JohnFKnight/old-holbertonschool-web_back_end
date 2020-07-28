#!/usr/bin/python3
""" LFUCache module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class:
    """

    def __init__(self):
        """ Override superclass __init__ """
        super(LFUCache, self).__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add to cache disctionary
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.cache_data.popitem(last=False)[0]))
            # self.cache_data.popitem(last=False)

    def get(self, key):
        """ Get value from cache
        """
        if key is None or not key:
            return
        return self.cache_data.get(key)
