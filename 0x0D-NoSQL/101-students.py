#!/usr/bin/env python3
""" returns all students sorted by average score."""


def top_students(mongo_collection):
    """ returns all students sorted by average score."""
    return db.mongo_collections.aggregate(
        {$group: {name: "$name", score: {$avg, 1}}},
        {$sort: {score, -1}}
        )
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
