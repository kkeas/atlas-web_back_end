#!/usr/bin/python3

"""FIFO caching class that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """First In First Out Class"""

    def __init__(self):
        """initialize FIFOCache"""
        super().__init__()
        """initialize parent class"""
        self.cache_list = []

    def put(self, key, item):
        """assigns the item value for the key in cache_list"""
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    oldest_key = next(iter(self.cache_data))
                    print(f"DISCARD: {oldest_key}")
                    del self.cache_data[oldest_key]
                self.cache_list.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """return the value linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            pass
