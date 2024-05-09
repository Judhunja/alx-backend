#!/usr/bin/env python3
"""This module contains a class LIFOCache"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implements LIFO caching where the last item to be used
    is the first to be removed from cache"""

    def __init__(self):
        """Initializes class LIFOCache"""
        super().__init__()
        self.cache_data = {}
        self.order_items = []

    def put(self, key, item):
        """Inserts into cache_data"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.order_items.append(key)
            if len(self.cache_data.items()) > super().MAX_ITEMS:
                discarded = self.order_items[-2]
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")

    def get(self, key):
        """Returns value associated with a key"""
        if key is None:
            return None
        else:
            return self.cache_data.get(key, None)
