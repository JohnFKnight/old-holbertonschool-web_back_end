#!/usr/bin/env python3

from pymongo import MongoClient

def list_all(mongo_collection):
    if not mongo_collection:
        return []
    return mongo_collection.find()
