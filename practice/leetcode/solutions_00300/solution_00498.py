#!/usr/bin/env python3

"""LeetCode solution 00498."""

import unittest
from collections import defaultdict


class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        row = len(mat)
        col = len(mat[0])

        if row == col == 1:
            return [mat[0][0]]

        d = defaultdict(list)

        for i in range(row):
            for j in range(col):
                key = i+j
                d[key].append(mat[i][j])

        res = []
        for diag in d:
            if diag % 2 == 0:
                res = res + d[diag][::-1]
            else:
                res = res + d[diag]

        return res


class Solution2(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        rows = len(mat)
        cols = len(mat[0])
        result = []

        row = 0
        col = 0
        direction = 1

        for _ in range(rows * cols):
            result.append(mat[row][col])

            if direction == 1:
                if col == cols - 1:
                    row += 1
                    direction = -1
                elif row == 0:
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            else:
                if row == rows - 1:
                    col += 1
                    direction = 1
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

        return result


class TestSolution(unittest.TestCase):
    def test_findDiagonalOrder(self):
        cases = [
            (
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [1, 2, 4, 7, 5, 3, 6, 8, 9],
            ),
            (
                [[1, 2], [3, 4]],
                [1, 2, 3, 4],
            ),
            (
                [[1, 2, 3], [4, 5, 6]],
                [1, 2, 4, 5, 3, 6],
            ),
            (
                [[1, 2], [3, 4], [5, 6]],
                [1, 2, 3, 5, 4, 6],
            ),
            (
                [[1]],
                [1],
            ),
        ]

        for solution_class in (Solution, Solution2):
            solution = solution_class()

            for mat, expected in cases:
                self.assertListEqual(solution.findDiagonalOrder(mat), expected)


if __name__ == '__main__':
    unittest.main()
