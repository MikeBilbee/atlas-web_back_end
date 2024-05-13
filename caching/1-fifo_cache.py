#!/bin/bash/env python3
"""
A class FIFOCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A basic FIFO caching system
    """

    def __init__(self):
        """ Initialize """

        super().__init__()

    def put(self, key, item):
        """Adding/Removing Cache data """

        if key or item is not None:
            mycache = self.get(key)
            if mycache is None:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    delete = list(self.cache_data.keys())[0]
                    del self.cache_data[delete]
                    print("DISCARD: {}".format(delete))
                    
            self.cache_data[key] = item

    def get(self, key):
        """
            modify cache data

            Args:
                key: of the dict

            Return:
                value of the key
        """

        mycache = self.cache_data.get(key)
        return mycache
