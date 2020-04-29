#!/usr/bin/env python

import unittest


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        if len(nums) == 1:
            return

        pivotal = len(nums) - 2
        while pivotal >= 0 and nums[pivotal] >= nums[pivotal+1]:
            pivotal -= 1
        if pivotal == -1:
            nums.sort()
        else:
            for i in reversed(range(pivotal + 1, len(nums))):
                if nums[i] > nums[pivotal]:
                    nums[pivotal], nums[i] = nums[i], nums[pivotal]
                    break
            nums[pivotal+1:] = reversed(nums[pivotal + 1:])


class TestSolution(unittest.TestCase):

    def test_nextPermutation(self):
        nums = [1, 2, 3]
        solution = Solution()
        solution.nextPermutation(nums)
        self.assertListEqual(nums, [1, 3, 2])


if __name__ == '__main__':
    unittest.main()
