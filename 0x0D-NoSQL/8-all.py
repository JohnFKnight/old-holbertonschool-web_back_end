#!/usr/bin/env python3
""" List all documents in a MongoDB collection """

from pymongo import MongoClient


def list_all(mongo_collection):
    """ Return collections.find() """
    if not mongo_collection:
        return []
    return mongo_collection.find()
