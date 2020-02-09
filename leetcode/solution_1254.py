#!/usr/bin/env python

import unittest


class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(matrix, sr, sc):
            if 0 <= sr < len(matrix) and 0 <= sc < len(matrix[0]) and not matrix[sr][sc]:
                matrix[sr][sc] = 1

                dfs(matrix, sr + 1, sc)
                dfs(matrix, sr - 1, sc)
                dfs(matrix, sr, sc + 1)
                dfs(matrix, sr, sc - 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[0])-1) and not grid[i][j]:
                    dfs(grid, i, j)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    dfs(grid, i, j)
                    res += 1

        return res


class TestSolution(unittest.TestCase):

    def test_closedIsland(self):
        grid = [[1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0]]
        grid2 = [[0, 0, 1, 0, 0],
                 [0, 1, 0, 1, 0],
                 [0, 1, 1, 1, 0]]

        solution = Solution()
        self.assertEqual(solution.closedIsland(grid), 2)
        self.assertEqual(solution.closedIsland(grid2), 1)


if __name__ == '__main__':
    unittest.main()
