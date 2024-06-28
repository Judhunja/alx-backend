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
        discard the most frequently used item, if there are more than
        one key that is least frequently used, discard the least recently
        used item"""
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.order_items.remove(key)
                self.order_items.append(key)
                self.number_used[key] += 1
            elif len(self.cache_data.items()) >= super().MAX_ITEMS:
                # keys = key for key in number_used.keys()

                minimum = min(self.number_used.values())
                min_val = [k for k, v in self.number_used.items()
                           if v == minimum]

                if len(min_val) > 1:
                    # if more than one val in min_val then remove the value
                    # in min_val that appears first in the self.order_items
                    # since that would be the least recently used item as
                    # it was added to self.order_items later
                    for k in min_val:
                        if k in self.order_items:
                            delkey = k
                        break

                else:
                    delkey = min_val[0]

                delkey = min_val[0]
                self.cache_data.pop(delkey)
                print(f"DISCARD: {delkey}")
                self.number_used.pop(delkey)
                self.cache_data[key] = item
                self.order_items.append(key)
                self.number_used[key] = 1

            else:
                self.cache_data[key] = item
                self.order_items.append(key)
                self.number_used[key] = 1

    def get(self, key):
        """Returns value associated with a particular key"""
        if key is None or self.cache_data.get(key, None) is None:
            return None
        else:
            self.order_items.remove(key)
            self.order_items.append(key)
            self.number_used[key] = self.number_used.get(key, 0) + 1
            return self.cache_data[key]
