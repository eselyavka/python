#!/usr/bin/env python

import unittest

class Solution(object):
    def _rec(self, nums, n):
        if n < len(nums):
            return max(nums[n] + self._rec(nums, n+2), self._rec(nums, n+1))
        return 0

    def rob_rec(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        return max(self._rec(nums, 0), self._rec(nums, 1))

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prevMax = currMax = 0

        for num in nums:
            currMax, prevMax = max(prevMax + num, currMax), currMax

        return currMax

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.arr1 = [5, 1, 2, 6, 20, 2]
        self.arr2 = [53, 1, 12, 65, 200, 2, 7, 90, 100, 54]
        self.arr3 = [1, 2, 3, 4]
        self.arr4 = [1, 1, 1, 1]
        self.arr5 = [1, 3, 1]
        self.arr6 = [2, 1, 1, 2]

    def test_matrixReshape(self):
        solution = Solution()

        self.assertEqual(solution.rob(self.arr1), 27)
        self.assertEqual(solution.rob(self.arr2), 409)
        self.assertEqual(solution.rob(self.arr3), 6)
        self.assertEqual(solution.rob(self.arr4), 2)
        self.assertEqual(solution.rob(self.arr5), 3)
        self.assertEqual(solution.rob(self.arr6), 4)

        self.assertEqual(solution.rob_rec(self.arr1), 27)
        self.assertEqual(solution.rob_rec(self.arr2), 409)
        self.assertEqual(solution.rob_rec(self.arr3), 6)
        self.assertEqual(solution.rob_rec(self.arr4), 2)
        self.assertEqual(solution.rob_rec(self.arr5), 3)
        self.assertEqual(solution.rob_rec(self.arr6), 4)

if __name__ == '__main__':
    unittest.main()
