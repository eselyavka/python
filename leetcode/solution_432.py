#!/usr/bin/env python

import unittest
from collections import defaultdict

class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_keys = defaultdict(int)
        self.dict_cnt = defaultdict(set)

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.dict_keys:
            curr, _next = self.dict_keys[key], self.dict_keys[key] + 1
            self.dict_cnt[curr].remove(key)
            self.dict_cnt[_next].add(key)
            if not self.dict_cnt[curr]:
                self.dict_cnt.pop(curr)
        else:
            self.dict_cnt[1].add(key)

        self.dict_keys[key] += 1

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.dict_keys:
            if self.dict_keys[key] - 1 == 0:
                self.dict_keys.pop(key)
                self.dict_cnt[1].remove(key)
                if not self.dict_cnt[1]:
                    self.dict_cnt.pop(1)
            else:
                curr, prev = self.dict_keys[key], self.dict_keys[key] - 1
                self.dict_cnt[curr].remove(key)
                self.dict_cnt[prev].add(key)
                self.dict_keys[key] -= 1
                if not self.dict_cnt[curr]:
                    self.dict_cnt.pop(curr)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if not self.dict_cnt:
            return ''

        _max = sorted(self.dict_cnt)[-1]
        res = self.dict_cnt[_max].pop() if _max else ''

        if res:
            self.dict_cnt[_max].add(res)

        return res

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if not self.dict_cnt:
            return ''

        _min = sorted(self.dict_cnt)[0]
        res = self.dict_cnt[_min].pop() if _min else ''

        if res:
            self.dict_cnt[_min].add(res)

        return res

class TestSolution(unittest.TestCase):

    def test_AllOne(self):
        solution = AllOne()

        self.assertEqual(solution.getMaxKey(), '')
        self.assertTrue(solution.getMinKey() == '')

        solution.inc('A')
        solution.inc('B')
        solution.inc('C')
        solution.inc('A')

        self.assertEqual(solution.getMaxKey(), 'A')
        self.assertTrue(solution.getMinKey() == 'C')

        solution.inc('B')
        solution.inc('B')
        solution.inc('C')
        solution.dec('A')
        solution.dec('A')

        self.assertEqual(solution.getMaxKey(), 'B')
        self.assertTrue(solution.getMinKey() == 'C')

        solution1 = AllOne()
        solution1.inc('a')

        for _ in range(4):
            solution1.inc('b')

        solution1.dec('b')
        solution1.dec('b')

        self.assertEqual(solution1.getMaxKey(), 'b')
        self.assertEqual(solution1.getMinKey(), 'a')

        solution2 = AllOne()
        solution2.inc('a')
        for _ in range(6):
            solution2.inc('b')
        self.assertEqual(solution2.getMaxKey(), 'b')
        self.assertEqual(solution2.getMinKey(), 'a')

if __name__ == '__main__':
    unittest.main()
