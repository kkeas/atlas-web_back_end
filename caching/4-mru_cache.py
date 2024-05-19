#!/usr/bin/python3

"""MRU caching system"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Most Recently Used Cache system"""

    def __init__(self):
        """initialize LIFOCache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """move key to end of ordered dict"""
        if key is not None and item is not None:
            if key in self.cache_data:
                """last=False means move the key to the front(MRU)"""
                self.cache_data.move_to_end(key, last=False)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    """remove last item in OrderedDict"""
                    oldest_key = next(reversed(self.cache_data))
                    print(f"DISCARD: {oldest_key}")
                    del self.cache_data[oldest_key]
                self.cache_data[key] = item

    def get(self, key):
        """return the value linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            pass
