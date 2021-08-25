from collections import deque

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.cache_update = deque()

    def get(self, key):
        if key in self.cache_update:
            self.cache_update.remove(key)
            self.cache_update.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        if len(self.cache) < self.capacity:
            if key in self.cache_update:
                self.cache_update.remove(key)
            self.cache_update.append(key)
            self.cache[key] = value
        else:
            if key in self.cache:
                self.cache_update.remove(key)
                self.cache_update.append(key)
                self.cache[key] = value            
            else:
                del self.cache[self.cache_update.popleft()]
                self.cache_update.append(key)
                self.cache[key] = value
