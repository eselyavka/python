#!/usr/bin/env python

import unittest

class Solution(object):
    def minCostClimbingStairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums and len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return min(nums)

        f0 = f1 = 0
        for num in nums:
            f0, f1 = num + min(f0, f1), f0

        return min(f0, f1)

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.arr1 = [10, 15, 20]
        self.arr2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        self.arr3 = [5]
        self.arr4 = [10, 9]

    def test_minCostClimbingStairs(self):
        solution = Solution()

        self.assertEqual(solution.minCostClimbingStairs(self.arr1), 15)
        self.assertEqual(solution.minCostClimbingStairs(self.arr2), 6)
        self.assertEqual(solution.minCostClimbingStairs(self.arr3), 5)
        self.assertEqual(solution.minCostClimbingStairs(self.arr4), 9)

if __name__ == '__main__':
    unittest.main()
