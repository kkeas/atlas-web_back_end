#!/usr/bin/python3

"""Create a class BasicCache that inherits from BaseCaching"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """basic cache class that inherits from BaseCaching"""

    def put(self, key, item):
        """assign to cache_data the item value for the key"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """return the value linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            pass
