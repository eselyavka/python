#!/usr/bin/env python

import unittest

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort()
        i = 0
        while i < len(nums) - 2:
            if nums[i] == nums[i+1] == nums[i+2]:
                i += 3
            else:
                return nums[i]
        else:
            return nums[i]

class TestSolution(unittest.TestCase):

    def test_singleNumber(self):
        nums = [11, 11, 11, 3, 3, 3, 10, 6, 6, 6]
        nums2 = [1, 1, 1, 3, 3, 3, 10, 6, 6, 6]
        nums3 = [1, 3, 3, 3, 10, 10, 10, 6, 6, 6]
        solution = Solution()
        self.assertEqual(solution.singleNumber(nums), 10)
        self.assertEqual(solution.singleNumber(nums2), 10)
        self.assertEqual(solution.singleNumber(nums3), 1)

if __name__ == '__main__':
    unittest.main()
