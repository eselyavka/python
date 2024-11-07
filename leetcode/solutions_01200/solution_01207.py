#!/usr/bin/env python

import unittest
from collections import Counter


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c = Counter(arr)

        return len(c.values()) == len(set(c.values()))


class TestSolution(unittest.TestCase):

    def test_uniqueOccurrences(self):
        solution = Solution()
        self.assertTrue(solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]))


if __name__ == '__main__':
    unittest.main()
