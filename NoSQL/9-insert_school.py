#!/usr/bin/env python3
""" 9-insert_school """


def insert_school(mongo_collection, **kwargs):
    """ insert school """
    return mongo_collection.insert(**kwargs)
