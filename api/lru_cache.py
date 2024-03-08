from collections import OrderedDict
import threading
import time

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            if key not in self.cache:
                return None
            value, expiration_time = self.cache[key]
            if time.time() > expiration_time:
                del self.cache[key]
                return None
            return value

    def set(self, key, value, expiration):
        with self.lock:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            expiration_time = time.time() + expiration
            self.cache[key] = (value, expiration_time)
