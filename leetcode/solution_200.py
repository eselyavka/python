#!/usr/bin/env python

import unittest

class Solution(object):
    def dfs(self, grid, seen, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
            return False

        if grid[row][col] == '0' or seen[row][col]:
            return False

        seen[row][col] = True

        self.dfs(grid, seen, row, col+1)
        self.dfs(grid, seen, row, col-1)
        self.dfs(grid, seen, row+1, col)
        self.dfs(grid, seen, row-1, col)

        return True

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        seen = [[False for _ in range(len(grid[i]))] for i in range(len(grid))]

        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if self.dfs(grid, seen, row, col):
                    islands += 1

        return islands

class TestSolution(unittest.TestCase):
    def test_numIslands(self):
        solution = Solution()
        self.assertEqual(solution.numIslands([["1", "1", "0", "0", "0"],
                                              ["1", "1", "0", "0", "0"],
                                              ["0", "0", "1", "0", "0"],
                                              ["0", "0", "0", "1", "1"]]), 3)

if __name__ == '__main__':
    unittest.main()
