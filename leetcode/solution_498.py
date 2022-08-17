#!/usr/bin/env python

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


class TestSolution(unittest.TestCase):
    def test_findDiagonalOrder(self):
        solution = Solution()

        self.assertListEqual(solution.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                             [1, 2, 4, 7, 5, 3, 6, 8, 9])


if __name__ == '__main__':
    unittest.main()
