#!/usr/bin/env python3
""" LIFO Cache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that inherits from BaseCaching.
    Implements a LIFO (Last In, First Out) caching strategy.
    """

    def __init__(self):
        """
        Initialize the LIFOCache instance.
        Calls the parent class's __init__ to set up cache_data.
        """
        super().__init__()
        self.stack = []  # List to track keys in LIFO order.

    def put(self, key, item):
        """
        Add an item to the cache.
        If the number of items exceeds MAX_ITEMS, discard the last added item.
        Args:
            key: The key associated with the item.
            item: The item to store in the cache.
        Notes:
            If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the item if the key already exists.
                self.cache_data[key] = item
                # Update stack to move the key to the top.
                self.stack.remove(key)
                self.stack.append(key)
            else:
                # Add new key-value pair to the cache.
                self.cache_data[key] = item
                self.stack.append(key)

                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    # LIFO: Remove the last added key from the cache.
                    last_key = self.stack.pop(-2)
                    del self.cache_data[last_key]
                    print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        Args:
            key: The key associated with the item.
        Returns:
            The value in the cache linked to key, or None if key is invalid.
        """
        return self.cache_data.get(key, None)
