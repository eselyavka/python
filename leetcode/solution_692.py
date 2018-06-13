#!/usr/bin/env python

import unittest
from collections import defaultdict

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

        res = d.items()

        def comparator(x, y, rev=False):
            if x[1] > y[1]:
                return 1 if not rev else -1
            elif x[1] < y[1]:
                return -1 if not rev else 1
            return comparator((None, x[0]), (None, y[0]), rev=True)

        res.sort(cmp=comparator, reverse=True)

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
