"""
Simple LFU cache implementation in python
"""

import unittest

class LFUCache(object):
    """
    Class which implement LFU cache algorithm
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
        in_cache = key in self.cache
        if in_cache:
            self.hash_table[key] += 1
        return int(in_cache) or -1


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
                min_value = min(self.hash_table.values())
                for k in self.cache:
                    if self.hash_table[k] == min_value:
                        del self.cache[k]
                        del self.hash_table[k]
                        break
                self.cache[key] = value
                self.hash_table[key] = 1
        else:
            self.hash_table[key] += 1
            self.cache[key] = value

class TestLFUCache(unittest.TestCase):
    """
    Test for LFUCache
    """

    def setUp(self):
        self.lfu_cache = LFUCache(3)

    def test_get_no_values(self):
        """
        No values in LFU cache
        """
        self.assertEqual(self.lfu_cache.get(50), -1)

    def test_set_values(self):
        """
        Set values to hash
        """
        for i in range(3):
            self.lfu_cache.set(i, i+10)
        self.assertEqual(len(self.lfu_cache.cache), 3)

    def test_lru_1(self):
        """
        Evict entry from LFU cache
        """
        _ = [self.lfu_cache.set('val{}'.format(x), 10 * x) for x in range(1, 4)]
        _ = [self.lfu_cache.get('val1') for x in range(10)]
        _ = [self.lfu_cache.get('val2') for x in range(20)]
        self.lfu_cache.set('val4', 100)
        self.assertEqual(self.lfu_cache.get('val3'), -1)
        lfu_keys = self.lfu_cache.cache.keys()
        lfu_keys.sort()
        lfu_hash_table_weights = self.lfu_cache.hash_table.values()
        lfu_hash_table_weights.sort()
        self.assertEqual(lfu_keys, ['val1', 'val2', 'val4'])
        self.assertEqual(lfu_hash_table_weights, [1, 11, 21])

    def test_lru_2(self):
        """
        Evict entry from LFU cache
        """
        _ = [self.lfu_cache.set('val{}'.format(x), 10 * x) for x in range(1, 4)]
        _ = [self.lfu_cache.get('val1') for x in range(20)]
        _ = [self.lfu_cache.get('val2') for x in range(10)]
        _ = [self.lfu_cache.get('val3') for x in range(10)]
        self.lfu_cache.set('val4', 100)
        lfu_hash_table_weights = self.lfu_cache.hash_table.values()
        lfu_hash_table_weights.sort()
        self.assertTrue('val2' in self.lfu_cache.cache.keys() or
                        'val3' in self.lfu_cache.cache.keys())
        self.assertTrue(all([x in self.lfu_cache.cache.keys() for x in ['val1', 'val4']]))
        self.assertEqual(lfu_hash_table_weights, [1, 11, 21])

if __name__ == '__main__':
    unittest.main()
