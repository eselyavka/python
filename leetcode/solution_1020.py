#!/usr/bin/env python

import unittest


class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def dfs(matrix, sr, sc):
            if 0 <= sr < len(matrix) and 0 <= sc < len(matrix[0]) and matrix[sr][sc] == 1:
                matrix[sr][sc] = 0

                dfs(matrix, sr + 1, sc)
                dfs(matrix, sr - 1, sc)
                dfs(matrix, sr, sc + 1)
                dfs(matrix, sr, sc - 1)

        for i in range(len(A)):
            for j in range(len(A[i])):
                if (i == 0 or j == 0 or i == len(A)-1 or j == len(A[0])-1) and A[i][j] == 1:
                    dfs(A, i, j)

        res = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    res += 1

        return res


class TestSolution(unittest.TestCase):

    def test_numEnclaves(self):
        grid = [[0, 0, 0, 0],
                [1, 0, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0]]
        grid2 = [[0, 1, 1, 0],
                 [0, 0, 1, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 0]]

        solution = Solution()
        self.assertEqual(solution.numEnclaves(grid), 3)
        self.assertEqual(solution.numEnclaves(grid2), 0)


if __name__ == '__main__':
    unittest.main()
