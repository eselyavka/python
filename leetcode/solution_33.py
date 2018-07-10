#!/usr/bin/env python

import unittest

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 1:
            return 0 if target in nums else -1

        def _binary_search(l, r, elem):
            if l > r:
                return -1

            mid = (l+r)//2

            if nums[mid] == elem:
                return mid

            if nums[l] <= nums[mid]:
                if elem >= nums[l] and elem <= nums[mid]:
                    return  _binary_search(l, mid - 1, elem)

                return _binary_search(mid+1, r, elem)

            if elem > nums[mid] and elem <= nums[r]:
                return _binary_search(mid+1, r, elem)

            return _binary_search(l, mid-1, elem)

        return _binary_search(0, len(nums) - 1, target)

class TestSolution(unittest.TestCase):
    def test_search(self):
        solution = Solution()
        self.assertEqual(solution.search([0, 1, 2, 4, 5, 6, 7], 4), 3)
        self.assertEqual(solution.search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(solution.search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(solution.search([5, 6, 7, 0, 1, 2, 4], 5), 0)
        self.assertEqual(solution.search([3, 5, 1], 3), 0)
        self.assertEqual(solution.search([5], 3), -1)
        self.assertEqual(solution.search([5], 5), 0)
        self.assertEqual(solution.search([2, 1], 1), 1)

if __name__ == '__main__':
    unittest.main()
