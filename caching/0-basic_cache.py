#!/usr/bin/env python3
"""
A class BasicCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):

    """
    A basic cache system
    """

    def put(self, key, item):

        """
        Adds an item to the cache.

        Args:
            key: The key to associate with the item.
            item: The item to store.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):

        """
        Retrieves an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The cached item, or None if the key doesn't exist.
        """
        
        return self.cache_data.get(key, None)
