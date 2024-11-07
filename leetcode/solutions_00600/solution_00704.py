#!/usr/bin/env python

import unittest

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1

class TestSolution(unittest.TestCase):
    def test_search(self):
        solution = Solution()
        self.assertEqual(solution.search([-1, 0, 3, 5, 9, 12], 9), 4)

if __name__ == '__main__':
    unittest.main()
