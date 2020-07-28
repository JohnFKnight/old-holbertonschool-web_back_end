#!/usr/bin/python3
""" MRUCache module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class:
    """

    def __init__(self):
        """ Override superclass __init__ """
        super(MRUCache, self).__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add to cache disctionary
        """
        cash = self.cache_data
        if key is None or item is None:
            return
        clen = len(cash)
        if key not in cash and clen >= BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(cash.popitem(last=True)[0]))
        cash[key] = item

    def get(self, key):
        """ Get value from cache
        """
        if key is None or not key:
            return
        return self.cache_data.get(key)
