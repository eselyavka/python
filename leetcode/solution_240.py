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
        self.assertTrue(solution.searchMatrix([[1, 4, 7, 11, 15],
                                               [2, 5, 8, 12, 19],
                                               [3, 6, 9, 16, 22],
                                               [10, 13, 14, 17, 24],
                                               [18, 21, 23, 26, 30]], 5))

        self.assertFalse(solution.searchMatrix([[1, 4, 7, 11, 15],
                                                [2, 5, 8, 12, 19],
                                                [3, 6, 9, 16, 22],
                                                [10, 13, 14, 17, 24],
                                                [18, 21, 23, 26, 30]], 20))


if __name__ == '__main__':
    unittest.main()
