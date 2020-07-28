#!/usr/bin/python3
""" LIFOCache module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class:
    """

    def __init__(self):
        """ Override superclass __init__ """
        super(LIFOCache, self).__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add to cache disctionary
        """
        cash = self.cache_data
        if key is None or item is None:
            return
        clen = len(cash)
        # print("len: ", clen)
        if key not in cash and clen >= BaseCaching.MAX_ITEMS:
            # self.remove_newest
            print("DISCARD: {}".format(cash.popitem(last=True)[0]))
        cash[key] = item

    # def remove_newest(self):
    #     """
    #     Remove the entry that has the newest accessed date
    #     """
    #     newest_entry = None
    #     for key in self.cache_data:
    #         if newest_entry is None:
    #             newest_entry = key
    # if self.cache_data[key]['date_accessed'] > self.cache_data[newest_entry][
    #             'date_accessed']:
    #             newest_entry = key
    #     print("DISCARD: {}".format(self.cache_data.pop(newest_entry)))

    def get(self, key):
        """ Get value from cache
        """
        if key is None or not key:
            return
        return self.cache_data.get(key)
