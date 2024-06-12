#!/usr/bin/env python3
""" Updates all topics """


def update_topics(mongo_collection, name, topics):
    """ Updates all topics of a school document based on name """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
