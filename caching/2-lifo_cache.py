#!/usr/bin/python3

"""LIFOCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Last In First Out Caching System"""

    def __init__(self):
        """initialize LIFOCache"""
        super().__init__()
        """initialize parent class"""
        self.cache_list = []

    def put(self, key, item):
        """put function to remove last key """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_list.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                newest_key = self.cache_list.pop()
                print(f"DISCARD: {newest_key}")
                del self.cache_data[newest_key]
            self.cache_data[key] = item
            self.cache_list.append(key)

    def get(self, key):
        """return the value linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            pass
