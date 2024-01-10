#!/usr/bin/python3

"""Create a class BasicCache that inherits from BaseCaching"""


class BaseCaching:
    def __init__(self):
        self.cache_data = {}

class BasicCache(BaseCaching):
    def put(self, key, item):
        self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key, None)
