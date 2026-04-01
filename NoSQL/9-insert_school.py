#!/usr/bin/env python3
""" 9-insert_school """


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection with kwargs."""
    return mongo_collection.insert(kwargs)
