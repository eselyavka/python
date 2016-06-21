"""
Simple LRU cache implementation in python
"""

import unittest
import random

class LRUCache(object):
    """
    Class which implement LRU cache algorithm
    """

    def __init__(self, capacity):
        """
        :type capacity: int
        :rtype: None
        """
        self.capacity = capacity
        self.cache = dict()
        self.hash_table = dict()


    def get(self, key):
        """
        :type key: str
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

class TestLRUCache(unittest.TestCase):
    """
    Test for LRUCache
    """

    def setUp(self):
        self.lru_cache = LRUCache(10)

    def test_get_no_values(self):
        """
        No values in LRU cache
        """
        self.assertEqual(self.lru_cache.get(50), -1)

    def test_set_values(self):
        """
        Set values to hash
        """
        for i in range(10):
            self.lru_cache.set(i, i+10)
        self.assertEqual(len(self.lru_cache.cache), 10)

if __name__ == '__main__':
    unittest.main()
