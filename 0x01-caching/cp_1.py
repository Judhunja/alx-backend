#!/usr/bin/env python3
"""This module contains a class LFUCache"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Implements least frequently used caching system"""

    def __init__(self):
        """Initializes class LFUCache"""
        super().__init__()
        self.cache_data = {}
        self.order_items = []
        self.number_used = {}

    def put(self, key, item):
        """Sets item for key in cache_data. If cache_data is full,
        discard the most frequently used item"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order_items.remove(key)
                self.order_items.append(key)
            elif len(self.cache_data.items()) >= super().MAX_ITEMS:
                # keys = key for key in number_used.keys()
                if len(self.number_used.items()) > 1:
                    maximum = max(value for value in self.number_used.values())
                    max_val = []

                    for key in self.number_used.keys():
                        if self.cache_data[key] == maximum:
                            max_val.append(key)

                    if len(max_val) == 1:
                        self.cache_data.pop(max_val[0])
                        self.order_items.remove(max_val[0])
                        print(f"DISCARD: {max_val[0]}")
                        if len(self.cache_data.items()) < super().MAX_ITEMS:
                            self.cache_data[max_val[0]] = item
                            self.order_items.append(max_val[0])
                    else:
                        delkey = self.order_items[-1]
                        self.order_items.remove(delkey)
                        self.cache_data.pop(delkey)
                        print(f"DISCARD: {delkey}")
                        if len(self.cache_data.items()) < super().MAX_ITEMS:
                            self.cache_data[key] = item
                            self.order_items.append(key)
                else:
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
            self.number_used[key] = self.number_used.get(key, 0) + 1
            return self.cache_data[key]
