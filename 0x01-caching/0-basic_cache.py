#!/usr/bin/env python3
"""This module contains a class BasicCache"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Implements a caching system with no limits
    """
    """def __init__(self):
        """"Initializes BasicCache""""
        self.cache_data = super().cache_data"""

    def put(self, key, item):
        """Assigns self.chache_data the item value for key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns value in self.cache_data for key"""
        if key is None:
            return None
        else:
            return self.cache_data.get(key, None)
