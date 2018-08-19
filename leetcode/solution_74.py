#!/usr/bin/env python

import unittest

class Solution(object):
    def binary_search(self, arr, target):
        r = len(arr) - 1
        l = 0
        while l <= r:
            mid = (l+r) // 2
            if arr[mid] == target:
                return True
            elif target > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for row in matrix:
            if self.binary_search(row, target):
                return True

        return False

class TestSolution(unittest.TestCase):

    def test_searchMatrix(self):
        solution = Solution()
        self.assertTrue(solution.searchMatrix([
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]], 3))
        self.assertFalse(solution.searchMatrix([
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]], 13))

if __name__ == '__main__':
    unittest.main()
