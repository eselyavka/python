#!/usr/bin/env python

import unittest


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 1:
            return nums[0]

        def binary_search(l, r):
            if l > r:
                return -1

            mid = (l+r) // 2

            elem = nums[mid]

            # last is a smalleset, array rotated desc
            if mid == n - 1:
                return elem

            if nums[mid - 1] > elem and nums[mid + 1] > elem:
                return elem

            if nums[r] <= elem:
                return binary_search(mid + 1, r)

            return binary_search(l, mid - 1)

        return binary_search(0, n - 1)


class TestSolution(unittest.TestCase):

    def test_findMin(self):
        solution = Solution()

        self.assertEqual(solution.findMin([3, 4, 5, 1, 2]), 1)


if __name__ == '__main__':
    unittest.main()
