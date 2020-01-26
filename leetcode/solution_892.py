#!/usr/bin/env python

import unittest


class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])

        if row != col:
            return reduce(lambda x, y: sum(x) + sum(y), grid, [0])

        res = 0

        for i in range(row):
            for j in range(col):
                if not grid[i][j]:
                    continue
                res += grid[i][j] * 6
                res -= 2*(grid[i][j] - 1)

                if i < row - 1:
                    res -= 2 * min(grid[i][j], grid[i+1][j])

                if j < col - 1:
                    res -= 2 * min(grid[i][j], grid[i][j+1])

        return res


class TestSolution(unittest.TestCase):
    def test_surfaceArea(self):
        solution = Solution()
        self.assertEqual(solution.surfaceArea([[2]]), 10)
        self.assertEqual(solution.surfaceArea([[1, 5]]), 6)
        self.assertEqual(solution.surfaceArea([[1, 2], [3, 4]]), 34)


if __name__ == '__main__':
    unittest.main()
