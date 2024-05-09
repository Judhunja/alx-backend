#!/usr/bin/env python3
"""This module contains a class LRUCache"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implements Least Recently Used method of caching"""

    def __init__(self):
        """Initializes class LRUCache"""
        super().__init__()
        self.cache_data = {}
        self.order_items = []

    def put(self, key, item):
        """Assigns key and item in cache_data, discards least recently
        used item if cache_data is full"""
        if key is not None and item is not None:
            # if key is already there just update
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order_items.remove(key)
                self.order_items.append(key)
            elif len(self.cache_data.items()) >= super().MAX_ITEMS:
                delkey = self.order_items.pop(0)
                del self.cache_data[delkey]
                print(f"DISCARD: {delkey}")
                self.cache_data[key] = item
                self.order_items.append(key)
            else:
                self.cache_data[key] = item
                self.order_items.append(key)

    def get(self, key):
        """returns the value in cache_data associated with key"""
        if key is None or self.cache_data.get(key, None) is None:
            return None
        else:
            self.order_items.remove(key)
            self.order_items.append(key)
            return self.cache_data[key]
