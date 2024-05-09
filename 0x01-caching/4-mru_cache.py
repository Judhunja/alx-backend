#!/usr/bin/env python3
"""This module contains a class MRUCache"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Implements most recently used caching system"""

    def __init__(self):
        """Initializes class MRUCache"""
        super().__init__()
        self.cache_data = {}
        self.order_items = []

    def put(self, key, item):
        """Sets item for key in cache_data. If cache_data is full,
        discard the most recently used item"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order_items.remove(key)
                self.order_items.append(key)
            elif len(self.cache_data.items()) >= super().MAX_ITEMS:
                delkey = self.order_items[-1]
                self.order_items.remove(delkey)
                self.cache_data.pop(delkey)
                print(f"DISCARD: {delkey}")
                if len(self.cache_data.items()) < super().MAX_ITEMS:
                    self.cache_data[key] = item
                    self.order_items.append(key)
            else:
                self.cache_data[key] = item
                self.order_items.append(key)

    def get(self, key):
        """Returns value associated with a particular key"""
        if key is None or self.cache_data.get(key, None) is None:
            return None
        else:
            self.order_items.remove(key)
            self.order_items.append(key)
            return self.cache_data[key]
