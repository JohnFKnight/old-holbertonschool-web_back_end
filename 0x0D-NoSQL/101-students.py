#!/usr/bin/env python3
""" returns all students sorted by average score."""


def top_students(mongo_collection):
    """ returns all students sorted by average score."""
    return list(mongo.collection.find())

    # mongo_collection.aggregate ([
    #     {$group: {_id: "$name", score: {$avg, 1}}},
    #     {$sort: {_id, -1}}
    #     ])

    #     [
    #     {$unwind: "$topics"},
    #     {$group: {
    #         title: "$title",
    #         score: "$score"
    #     }},
    #     {$group: {
    #         avg_score: { $avg: "$score" }
    #     }}
    # ])
