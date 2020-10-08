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
                if seen[row][col]:
                    continue

                if self.dfs(grid, seen, row, col):
                    islands += 1

        return islands


class Solution2(object):
    def find(self, arr, x):
        if arr[x] == x:
            return x
        arr[x] = self.find(arr, arr[x])
        return arr[x]

    def union(self, arr, rank, x, y):
        xx = self.find(arr, x)
        yy = self.find(arr, y)
        if xx != yy:
            if rank[xx] > rank[yy]:
                arr[yy] = arr[xx]
            elif rank[yy] > rank[xx]:
                arr[xx] = arr[yy]
            else:
                arr[yy] = arr[xx]
                rank[xx] += 1

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])
        arr = [i for i in range(n*m)]
        rank = [0 for _ in range(n*m)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    if i > 0 and grid[i-1][j] == '1':
                        self.union(arr, rank, i * m + j, (i - 1) * m + j)
                    if j > 0 and grid[i][j - 1] == '1':
                        self.union(arr, rank, i * m + j, i * m + (j - 1))
        s = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    id_ = self.find(arr, i*m+j)
                    s.add(id_)
        return len(s)


class TestSolution(unittest.TestCase):
    def test_numIslands(self):
        solution = Solution()
        self.assertEqual(solution.numIslands([["1", "1", "0", "0", "0"],
                                              ["1", "1", "0", "0", "0"],
                                              ["0", "0", "1", "0", "0"],
                                              ["0", "0", "0", "1", "1"]]), 3)
        solution2 = Solution2()
        self.assertEqual(solution2.numIslands([["1", "1", "0", "0", "0"],
                                               ["1", "1", "0", "0", "0"],
                                               ["0", "0", "1", "0", "0"],
                                               ["0", "0", "0", "1", "1"]]), 3)


if __name__ == '__main__':
    unittest.main()
