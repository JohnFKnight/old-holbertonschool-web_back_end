#!/usr/bin/env python3
"""  inserts a new document in a collection based on kwargs"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ Insert into collection """
    if not mongo_collection:
        return []
    return mongo_collection.insert(kwargs)
