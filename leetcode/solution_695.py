#!/usr/bin/env python

import unittest

class Solution(object):
    def _rec(self, grid, seen, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return 0

        if grid[i][j] == 0 or seen[i][j]:
            return 0

        seen[i][j] = True

        return  (grid[i][j] +
                 self._rec(grid, seen, i+1, j) +
                 self._rec(grid, seen, i-1, j) +
                 self._rec(grid, seen, i, j+1) +
                 self._rec(grid, seen, i, j-1))

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = [[False for _ in range(len(grid[i]))] for i in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res = max(res, self._rec(grid, seen, i, j))
        return res

class TestSolution(unittest.TestCase):

    def test_maxAreaOfIsland(self):
        arr = [[0, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
        arr2 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

        solution = Solution()
        self.assertEqual(solution.maxAreaOfIsland(arr), 3)
        self.assertEqual(solution.maxAreaOfIsland(arr2), 6)

if __name__ == '__main__':
    unittest.main()
