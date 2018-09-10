#!/usr/bin/env python

import unittest

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        nums.sort()

        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

class TestSolution(unittest.TestCase):

    def test_maximumProduct(self):
        solution = Solution()

        self.assertEqual(solution.maximumProduct([1, 2]), 0)
        self.assertEqual(solution.maximumProduct([1, 2, 3]), 6)
        self.assertEqual(solution.maximumProduct([1, 2, 3, 4]), 24)

if __name__ == '__main__':
    unittest.main()
