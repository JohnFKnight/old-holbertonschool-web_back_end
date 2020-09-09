#!/usr/bin/env python3

from pymongo import MongoClient

def list_all(mongo_collection):
    if not mongo_collection:
        return []
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.mydb
    return db.mongo_collection.find()
