#!/usr/bin/env python

import unittest

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            return nums.index(max(nums))

        def binary_search():
            l = 0
            r = len(nums) - 1

            while r >= l:
                mid = (r+l) // 2

                if r == l:
                    return r

                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid+1]:
                    return mid

                if nums[mid] > nums[mid+1] and nums[mid-1] > nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return binary_search()

class TestSolution(unittest.TestCase):
    def test_findPeakElement(self):
        solution = Solution()

        self.assertEqual(solution.findPeakElement([1, 2, 3, 1]), 2)
        self.assertTrue(solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in [1, 5])
        self.assertEqual(solution.findPeakElement([2, 1]), 0)
        self.assertEqual(solution.findPeakElement([1, 2, 3]), 2)
        self.assertEqual(solution.findPeakElement([1, 2]), 1)
        self.assertTrue(solution.findPeakElement([1, 2, 1, 2, 1]) in [1, 3])

if __name__ == '__main__':
    unittest.main()
