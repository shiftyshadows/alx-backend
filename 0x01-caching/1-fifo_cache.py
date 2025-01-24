#!/usr/bin/env python3
""" This module defines the class: FIFOCache."""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that inherits from BaseCaching.
    Implements a FIFO (First In, First Out) caching strategy.
    """

    def __init__(self):
        """
        Initialize the FIFOCache instance.
        Calls the parent class's __init__ to set up cache_data.
        """
        super().__init__()
        self.keys_order = []  # Tracks the order of keys for FIFO.

    def put(self, key, item):
        """
        Add an item to the cache.
        If the number of items exceeds MAX_ITEMS, discard the oldest item.
        Args:
            key: The key associated with the item.
            item: The item to store in the cache.
        Notes:
            If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # If the key exists, update the item but keep the position.
                self.cache_data[key] = item
                return

            self.cache_data[key] = item
            self.keys_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # FIFO: Remove the first added key.
                oldest_key = self.keys_order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        Args:
            key: The key associated with the item.
        Returns:
            The value in the cache linked to key, or None if key is invalid.
        """
        return self.cache_data.get(key, None)
