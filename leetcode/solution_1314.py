#!/usr/bin/env python

import unittest


class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        row = len(mat)
        col = len(mat[0])
        res = [[None for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                elem = 0
                for r in range(max(i-K, 0), min(i+K, row - 1) + 1):
                    for c in range(max(j-K, 0), min(j+K, col - 1) + 1):
                        elem += mat[r][c]
                res[i][j] = elem

        return res


class TestSolution(unittest.TestCase):

    def test_matrixBlockSum(self):
        solution = Solution()
        self.assertListEqual(solution.matrixBlockSum(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1),
                             [[12, 21, 16], [27, 45, 33], [24, 39, 28]])


if __name__ == '__main__':
    unittest.main()
