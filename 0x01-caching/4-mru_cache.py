#!/usr/bin/env python3
""" MRU Cache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that inherits from BaseCaching.
    Implements an MRU (Most Recently Used) caching strategy.
    """

    def __init__(self):
        """
        Initialize the MRUCache instance.
        Calls the parent class's __init__ to set up cache_data.
        """
        super().__init__()
        self.usage_order = []  # Tracks usage order of keys for MRU.

    def put(self, key, item):
        """
        Add an item to the cache.
        If the number of items exceeds MAX_ITEMS, discard the most
        recently used.
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
                # Move the key to the end to mark it as recently used.
                self.usage_order.remove(key)
                self.usage_order.append(key)
            else:
                # Add new key-value pair to the cache.
                self.cache_data[key] = item
                self.usage_order.append(key)

                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    # MRU: Remove the most recently used key.
                    mru_key = self.usage_order.pop(-1)
                    del self.cache_data[mru_key]
                    print(f"DISCARD: {mru_key}")

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        Args:
            key: The key associated with the item.
        Returns:
            The value in the cache linked to key, or None if key is invalid.
        """
        if key in self.cache_data:
            # Mark the key as recently used.
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
