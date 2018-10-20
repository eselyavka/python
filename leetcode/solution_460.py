#!/usr/bin/env python

"""
Dummy LFU cache implementation in python
"""

import unittest
from collections import defaultdict

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
        self.count = defaultdict(int)
        self.freq = defaultdict(list)

    def get(self, key):
        """
        :type key: str
        :rtype: int
        """
        if not key in self.cache:
            return -1

        _freq = self.count[key]
        self.count[key] = _freq + 1
        self.freq[_freq].remove(key)

        if not self.freq[_freq]:
            self.freq.pop(_freq)

        self.freq[_freq + 1].append(key)

        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """

        if self.capacity == 0:
            return

        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                min_freq = min(self.freq.keys())
                key_to_remove = self.freq[min_freq].pop(0)

                if not self.freq[min_freq]:
                    self.freq.pop(min_freq)

                self.cache.pop(key_to_remove)
                self.count.pop(key_to_remove)

        _freq = self.count[key]

        if self.freq[_freq]:
            self.freq[_freq].remove(key)

        if not self.freq[_freq]:
            self.freq.pop(_freq)

        self.count[key] = _freq + 1
        self.cache[key] = value
        self.freq[_freq + 1].append(key)

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
            self.lfu_cache.put(i, i + 10)
        self.assertEqual(len(self.lfu_cache.cache), 3)

    def test_zero_size(self):
        """
        Zero size LFU cache
        """
        cache = LFUCache(0)
        cache.put(0, 0)
        self.assertEqual(cache.get(0), -1)

    def test_lfu_1(self):
        """
        Evict entry from LFU cache
        """
        _ = [self.lfu_cache.put('val{}'.format(x), 10 * x) for x in range(1, 4)]
        _ = [self.lfu_cache.get('val1') for x in range(10)]
        _ = [self.lfu_cache.get('val2') for x in range(20)]
        self.lfu_cache.put('val4', 100)
        self.assertEqual(self.lfu_cache.get('val3'), -1)
        lfu_keys = self.lfu_cache.cache.keys()
        lfu_keys.sort()
        lfu_hash_table_weights = self.lfu_cache.count.values()
        lfu_hash_table_weights.sort()
        self.assertEqual(lfu_keys, ['val1', 'val2', 'val4'])
        self.assertEqual(lfu_hash_table_weights, [1, 11, 21])

    def test_lfu_2(self):
        """
        Evict entry from LFU cache
        """
        _ = [self.lfu_cache.put('val{}'.format(x), 10 * x) for x in range(1, 4)]
        _ = [self.lfu_cache.get('val1') for x in range(20)]
        _ = [self.lfu_cache.get('val2') for x in range(10)]
        _ = [self.lfu_cache.get('val3') for x in range(10)]
        self.lfu_cache.put('val4', 100)
        lfu_hash_table_weights = self.lfu_cache.count.values()
        lfu_hash_table_weights.sort()
        self.assertTrue('val2' in self.lfu_cache.cache.keys() or
                        'val3' in self.lfu_cache.cache.keys())
        self.assertTrue(all([x in self.lfu_cache.cache.keys() for x in ['val1', 'val4']]))
        self.assertEqual(lfu_hash_table_weights, [1, 11, 21])

    def test_lfu_3(self):
        """
        Evict entry from LFU cache
        """
        cache = LFUCache(2)
        cache.put(2, 1)
        cache.put(3, 2)
        self.assertEqual(cache.get(3), 2)
        self.assertEqual(cache.get(2), 1)
        cache.put(4, 3)
        self.assertEqual(cache.get(2), 1)
        self.assertEqual(cache.get(3), -1)
        self.assertEqual(cache.get(4), 3)

    def test_lfu_4(self):
        """
        Evict entry from LFU cache
        """
        cache = LFUCache(10)

        operation = ["put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
                     "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get",
                     "put", "get", "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put",
                     "put", "get", "put", "put", "put", "put", "get", "put", "put", "get", "put", "put", "get", "put",
                     "put", "put", "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get",
                     "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "get", "get", "get", "put",
                     "put", "put", "get", "put", "put", "put", "get", "put", "put", "put", "get", "get", "get", "put",
                     "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
        data = [[10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
                [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3],
                [10, 11], [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27],
                [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10],
                [4, 15], [7, 22], [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6],
                [3, 4], [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8],
                [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19],
                [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26],
                [13, 28], [11, 26]]

        actual = []
        null = 'null'
        for _op, payload in zip(operation, data):
            if _op == 'put':
                cache.put(*payload)
                actual.append(null)
            else:
                actual.append(cache.get(*payload))

        expected = [null, null, null, null, null, -1, null, 19, 17, null, -1, null, null, null, -1, null, -1, 5, -1, 12,
                    null, null, 3, 5, 5, null, null, 1, null, -1, null, 30, 5, 30, null, null, null, -1, null, -1, 24,
                    null, null, 18, null, null, null, null, 14, null, null, 18, null, null, 11, null, null, null, null,
                    null, 18, null, null, -1, null, 4, 29, 30, null, 12, 11, null, null, null, null, 29, null, null,
                    null, null, 17, -1, 18, null, null, null, -1, null, null, null, 20, null, null, null, 29, 18, 18,
                    null, null, null, null, 20, null, null, null, null, null, null, null]

        self.assertListEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
