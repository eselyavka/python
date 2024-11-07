#!/usr/bin/env python

import unittest


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = [[False for _ in range(len(grid[i]))] for i in range(len(grid))]

        def island_area(matrix, sr, sc):
            if sr >= len(matrix) or sr < 0 or sc >= len(matrix[0]) or sc < 0:
                return 0

            if matrix[sr][sc] == 0 or seen[sr][sc]:
                return 0

            seen[sr][sc] = True

            return (matrix[sr][sc] +
                    island_area(matrix, sr + 1, sc) +
                    island_area(matrix, sr - 1, sc) +
                    island_area(matrix, sr, sc + 1) +
                    island_area(matrix, sr, sc - 1))

        max_possible = len(grid) * len(grid[0])
        max_local = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if max_local == max_possible:
                    return max_local
                max_local = max(max_local, island_area(grid, i, j))

        return max_local


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
