#!/usr/bin/env python

import unittest


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prev = 0
        for idx, num in enumerate(nums):
            nums[idx] = prev + num
            prev = nums[idx]

        return nums


class TestSo_runningSumlution(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertListEqual(solution.runningSum([1, 2, 3, 4]), [1, 3, 6, 10])


if __name__ == '__main__':
    unittest.main()
