#!/usr/bin/env python3
""" List all documents in a MongoDB collection """

from pymongo import MongoClient


def list_all(mongo_collection):
    """ Return collections.find() """
    if not mongo_collection:
        return []
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.mydb
    return db.mongo_collection.find()
