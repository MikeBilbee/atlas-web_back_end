#!/usr/bin/python3
"""
    A class LRUCache that inherits from BaseCaching and is a
    caching system: You must use self.cache_data - dictionary from the
    parent class BaseCaching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A basic LRU caching system"""
    def __init__(self):
        """initialize"""

        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data the item value for
        the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
        you must discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded and following
        by a new line"""
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS and key not in\
                    self.keys:
                del_key = self.keys.pop(0)
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))
            if key in self.keys:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn't exist in self.cache_data,
    return None"""
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key)
