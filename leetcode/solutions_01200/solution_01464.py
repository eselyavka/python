#!/usr/bin/env python

import unittest


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 2:
            return (nums[0]-1) * (nums[1] - 1)

        max_ = -1, -1

        for i, num in enumerate(nums):
            if num > max_[1]:
                max_ = i, num

        sec_max = -1

        for i, num in enumerate(nums):
            if num > sec_max and max_[0] != i:
                sec_max = num

        return (max_[1] - 1) * (sec_max - 1)


class TestSolution(unittest.TestCase):
    def test_maxProduct(self):
        solution = Solution()
        self.assertEqual(solution.maxProduct([10, 2, 5, 2]), 36)


if __name__ == '__main__':
    unittest.main()
