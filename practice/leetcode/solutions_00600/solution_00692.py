#!/usr/bin/env python3

"""LeetCode solution 00692."""

import unittest
from collections import defaultdict
from functools import cmp_to_key

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = defaultdict(int)

        for word in words:
            d[word] += 1

        res = list(d.items())

        def comparator(x, y, rev=False):
            if x[1] > y[1]:
                return 1 if not rev else -1
            elif x[1] < y[1]:
                return -1 if not rev else 1
            return comparator((None, x[0]), (None, y[0]), rev=True)

        res.sort(key=cmp_to_key(comparator), reverse=True)

        return [x[0] for x in res[:k]]

class TestSolution(unittest.TestCase):

    def test_topKFrequent(self):
        solution = Solution()

        words = ["i", "love", "leetcode", "i", "love", "coding"]
        words1 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]

        self.assertEqual(solution.topKFrequent(words, 2),
                         ["i", "love"])

        self.assertEqual(solution.topKFrequent(words1, 4),
                         ["the", "is", "sunny", "day"])

        self.assertEqual(solution.topKFrequent(["aaa", "aa", "a"], 1), ["a"])

if __name__ == '__main__':
    unittest.main()
