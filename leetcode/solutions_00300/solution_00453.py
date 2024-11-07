#!/usr/bin/env python

import unittest

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()

        for i in range(len(nums) - 1, 0, -1):
            res += nums[i] - nums[0]

        return res

class TestSolution(unittest.TestCase):

    def test_monMoves(self):
        solution = Solution()
        self.assertEqual(solution.minMoves([1, 2, 3]), 3)

if __name__ == '__main__':
    unittest.main()
