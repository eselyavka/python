#!/usr/bin/env python

import unittest

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nums.sort()

        for i in range(1, len(nums)):
            if i % 2 == 0:
                buf = nums[i]
                nums[i] = nums[i-1]
                nums[i-1] = buf

class TestSolution(unittest.TestCase):

    def test_wiggleSort(self):
        arr = [3, 5, 2, 1, 6, 4]
        solution = Solution()
        solution.wiggleSort(arr)
        self.assertEqual(arr, [1, 3, 2, 5, 4, 6])

if __name__ == '__main__':
    unittest.main()
