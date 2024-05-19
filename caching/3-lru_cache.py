#!/usr/bin/python3

"""LRUCache that inherits from BaseCaching and is a caching system"""

from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Least Recently Used algorithm caching system"""

    def __init__(self):
        """initialize LIFOCache"""
        super().__init__()
        """initialize parent class"""
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """move key to end of ordered dict"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    oldest_key = next(iter(self.cache_data))
                    print(f"DISCARD: {oldest_key}")
                    del self.cache_data[oldest_key]
                self.cache_data[key] = item

    def get(self, key):
        """return the value linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            pass
