#!/usr/bin/env python

import unittest

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        if nums[0] != 0:
            return 0

        if nums[-1] != len(nums):
            return len(nums)

        i = 0
        while i < len(nums):
            if nums[i] - nums[i-1] > 1:
                return nums[i] - 1
            i += 1

class TestSolution(unittest.TestCase):
    def test_missingNumber(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([3, 0, 1]), 2)
        self.assertEqual(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

if __name__ == '__main__':
    unittest.main()
