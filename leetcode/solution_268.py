#!/usr/bin/env python

import unittest

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]+1 if nums[0] == 0 else nums[0]-1

        i = 1
        nums.sort()

        while i < len(nums):
            if nums[i] - nums[i-1] > 1:
                return nums[i] - 1
            i += 1

        return nums[len(nums)-1] + 1 if nums[0] == 0 else 0

class TestSolution(unittest.TestCase):
    def test_missingNumber(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([3, 0, 1]), 2)
        self.assertEqual(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

if __name__ == '__main__':
    unittest.main()
