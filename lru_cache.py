"""Simple LRU cache implementation in python"""
class LRUCache(object):
    """Class which implement LRU cache algorithm"""

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict()
        self.hash_table = dict()


    def get(self, key):
        """
        :rtype: int
        """

        return int(key in self.cache) or -1


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """

        if self.get(key) == -1:
            if len(self.cache) < self.capacity:
                self.cache[key] = value
                self.hash_table[key] = 1
            else:
                for k in self.cache:
                    if min(self.cache.values()) == self.cache[k]:
                        del self.cache[k]
                        del self.hash_table[k]
                        break
                self.cache[key] = value
                self.hash_table[key] = 1
        else:
            self.hash_table[key] += 1
            self.cache[key] = value
