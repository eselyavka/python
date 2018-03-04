#!/usr/bin/env python

import unittest

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = float('-inf')
        max_ending_here = 0

        for i in nums:
            max_ending_here = max_ending_here + i

            max_so_far = max(max_ending_here, max_so_far)

            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far

class TestSolution(unittest.TestCase):

    def test_singleNumber(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        nums2 = [-1]
        solution = Solution()
        self.assertEqual(solution.maxSubArray(nums), 6)
        self.assertEqual(solution.maxSubArray(nums2), -1)

if __name__ == '__main__':
    unittest.main()
