#!/usr/bin/env python3
""" This module defines the class:BasicCache."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching.
    This system has no limit on the number of items stored in the cache.
    """
    def put(self, key, item):
        """
        Add an item to the cache.
        Args:
            key: The key associated with the item.
            item: The item to store in the cache.
        Notes:
            If key or item is None, the method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        Args:
            key: The key associated with the item.
        Returns:
            The value in the cache linked to key, or None if key is invalid.
        """
        return self.cache_data.get(key, None)
