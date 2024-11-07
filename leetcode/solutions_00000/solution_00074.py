#!/usr/bin/env python

import unittest


class Solution(object):
    def binary_search(self, arr, target):
        r = len(arr) - 1
        l = 0
        while l <= r:
            mid = (l + r) // 2
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


class Solution2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix)
        c = len(matrix[0])

        top, bottom = 0, r - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if not top <= bottom:
            return False

        low, high = 0, c - 1

        row = (top + bottom) // 2

        while low <= high:
            mid = (low + high) // 2
            if target == matrix[row][mid]:
                return True

            if target > matrix[row][mid]:
                low = mid + 1
            else:
                high = mid - 1

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

        solution2 = Solution2()
        self.assertTrue(solution2.searchMatrix([
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]], 3))
        self.assertFalse(solution2.searchMatrix([
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]], 13))


if __name__ == '__main__':
    unittest.main()
