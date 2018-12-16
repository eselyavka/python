#!/usr/bin/env python

import unittest

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        res = [-1, -1]

        if len(nums) == 1:
            return [0, 0] if target == nums[0] else res

        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == target and nums[right] == target:
                return [left, right]
            elif nums[left] == target:
                right -= 1
            elif nums[right] == target:
                left += 1
            else:
                right -= 1
                left += 1

        return [-1, -1]


class TestSolution(unittest.TestCase):
    def test_searchRange(self):
        solution = Solution()
        self.assertEqual(solution.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])
        self.assertEqual(solution.searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1])
        self.assertEqual(solution.searchRange([7, 7, 7, 7, 7, 7], 7), [0, 5])
        self.assertEqual(solution.searchRange([1, 2, 3, 4, 7, 7], 7), [4, 5])
        self.assertEqual(solution.searchRange([7, 7, 17, 27, 37, 47], 7), [0, 1])
        self.assertEqual(solution.searchRange([6, 7, 17, 27, 37, 47], 6), [0, 0])
        self.assertEqual(solution.searchRange([1], 1), [0, 0])




if __name__ == '__main__':
    unittest.main()
