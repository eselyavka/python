#!/usr/bin/env python

import unittest


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        dup = -1
        missing = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                dup = nums[i]
            elif nums[i] > nums[i-1] + 1:
                missing = nums[i-1] + 1
        return [dup, len(nums)] if nums[-1] != len(nums) else [dup, missing]


class TestSolution(unittest.TestCase):
    def test_findErrorNums(self):
        solution = Solution()
        self.assertListEqual(solution.findErrorNums([1, 2, 2, 4]), [2, 3])
        self.assertListEqual(solution.findErrorNums([2, 2]), [2, 1])
        self.assertListEqual(solution.findErrorNums([1, 1]), [1, 2])


if __name__ == '__main__':
    unittest.main()
