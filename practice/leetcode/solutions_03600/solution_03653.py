#!/usr/bin/env python3

"""LeetCode solution 03653."""

from functools import reduce
from operator import xor

import unittest


class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        for q in queries:
            l, r, k, v = q
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % (10**9 + 7)
                idx += k

        return reduce(xor, nums)


class TestSolution(unittest.TestCase):
    def test_xorAfterQueries(self):
        solution = Solution()
        self.assertEqual(solution.xorAfterQueries([1, 1, 1], [[0, 2, 1, 4]]), 4)
        self.assertEqual(solution.xorAfterQueries([2, 3, 1, 5, 4], [[1, 4, 2, 3], [0, 2, 1, 2]]), 31)


if __name__ == '__main__':
    unittest.main()
