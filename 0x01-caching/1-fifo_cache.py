#!/usr/bin/env python3
"""This module contains a class FIFOCache"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Implements a FIFO caching system"""

    def __init__(self):
        """Initializes class FIFOCache"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        Assigns values to the dict.
        If the number of items is greater than a given
        parameter, the first item put in the dict must be
        discarded and the key printed
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data.items()) > super().MAX_ITEMS:
                discarded = next(iter(self.cache_data.keys()))
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")

    def get(self, key):
        """Returns the value for a key in self.cache_data"""
        if key is None:
            return None
        else:
            return self.cache_data.get(key, None)
