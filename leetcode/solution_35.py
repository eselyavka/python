#!/usr/bin/env python

import unittest

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        r = 0
        l = len(nums) - 1
        pos = -1
        element = None
        find = False
        while not find and l >= r:
            mid = (r+l)//2
            if nums[mid] == target:
                pos = mid
                find = True
            elif target > nums[mid]:
                r = mid + 1
                element = nums[mid]
            else:
                l = mid - 1
                element = nums[mid]

        if pos < 0:
            if target > element:
                pos = mid+1
            else:
                pos = mid
        return pos

class TestSolution(unittest.TestCase):

    def test_searchInsert(self):
        solution = Solution()
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 7), 4)
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 0), 0)
        self.assertEqual(solution.searchInsert([1, 3], 2), 1)

if __name__ == '__main__':
    unittest.main()
