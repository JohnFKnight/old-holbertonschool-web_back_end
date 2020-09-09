#!/usr/bin/env python3
""" returns all students sorted by average score."""


def top_students(mongo_collection):
    """ returns all students sorted by average score."""
    # return list(mongo.collection.find())

    return mongo_collection.aggregate([
        {"$group": {_id: "$name", score: {"$avg", 1}}},
        {"$sort": {_id, -1}}])

    # pipeline = [
    # {$unwind: "$topics"},
    # {$group: {
    #     _id: "$topics[$score]",
    #     score: {$avg, 1}
    # }},
    # {$group: {
    #     avg_score: { $avg: "$score" }
    # }}
    # ])
