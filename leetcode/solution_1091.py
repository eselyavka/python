#!/usr/bin/env python

import unittest
from collections import deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid) - 1
        m = len(grid[0]) - 1

        if grid[0][0] == 1 or grid[n][m] == 1:
            return -1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1,1)]

        def neighbours(i, j):
            for di, dj in directions:
                new_i = i + di
                new_j = j + dj
                if not(0 <= new_i <= n and 0 <= new_j <= m):
                    continue
                if grid[new_i][new_j] == 1:
                    continue
                yield new_i, new_j

        q = deque([(0, 0, 1)])
        visited = {(0, 0)}

        while q:
            row, col, d = q.popleft()
            if row == n and col == m:
                return d
            for neighbour in neighbours(row, col):
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                q.append(neighbour + tuple([d + 1]))

        return -1


class TestSolution(unittest.TestCase):
    def test_shortestPathBinaryMatrix(self):
        solution = Solution()

        self.assertEqual(solution.shortestPathBinaryMatrix([[0, 1], [1, 0]]), 2)


if __name__ == '__main__':
    unittest.main()
