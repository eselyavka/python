#!/usr/bin/env python

import unittest

class Solution(object):
    def splitArrayEqualSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[]]
        """
        sum_nums = sum(nums)
        sub_sum = 0

        for i in range(len(nums) - 1, -1, -1):
            sub_sum += nums[i]
            if sum_nums - sub_sum == sub_sum:
                return [nums[:i], nums[i:]]

        return []

class TestSolution(unittest.TestCase):
    def test_splitArrayEqualSum(self):
        solution = Solution()

        actual = solution.splitArrayEqualSum([1, 2, 3, 4, 5, 5])
        self.assertListEqual(actual, [[1, 2, 3, 4], [5, 5]])

if __name__ == '__main__':
    unittest.main()
