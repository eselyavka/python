#!/usr/bin/env python

import unittest
from collections import Counter


class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        c = Counter(arr)
        max_ = -1
        for num in arr:
            if c[num] == num:
                max_ = max(num, max_)
        return max_


class TestSolution(unittest.TestCase):

    def test_findLucky(self):
        solution = Solution()
        self.assertEqual(solution.findLucky([2, 2, 3, 4]), 2)


if __name__ == '__main__':
    unittest.main()
