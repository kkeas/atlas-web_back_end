#!/usr/bin/python3

"""Create a class BasicCache that inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):

    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            pass
