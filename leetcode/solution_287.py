#!/usr/bin/env python

import unittest

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        nums.sort()
        i = 0

        while i < n:
            if nums[i] == nums[i+1]:
                return nums[i]

            i += 1

class TestSolution(unittest.TestCase):
    def test_findDuplicate(self):
        solution = Solution()
        self.assertEqual(solution.findDuplicate([1, 3, 4, 2, 2]), 2)
        self.assertEqual(solution.findDuplicate([3, 1, 3, 4, 2]), 3)

if __name__ == '__main__':
    unittest.main()
