#!/usr/bin/env python3
""" 10-update_topics """


def update_topics(mongo_collection, name, topics):
    """ updating the topics """
    return mongo_collection.update(
        {"name": name},
        {"$set": {"topics": topics }},
        {multi: true}
    )
