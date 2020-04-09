#!/usr/bin/env python

import unittest


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_max = []
        col_max = []
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            max_row = float('-inf')
            max_col = float('-inf')
            for j in range(col):
                max_row = max(grid[i][j], max_row)
                max_col = max(grid[j][i], max_col)
            row_max.append(max_row)
            col_max.append(max_col)

        res = 0
        for i in range(row):
            for j in range(col):
                curr = min(row_max[i], col_max[j])
                res += abs(grid[i][j] - curr)

        return res


class TestSolution(unittest.TestCase):

    def test_maxIncreaseKeepingSkyline(self):
        solution = Solution()
        self.assertEqual(solution.maxIncreaseKeepingSkyline([[3, 0, 8, 4],
                                                             [2, 4, 5, 7],
                                                             [9, 2, 6, 3],
                                                             [0, 3, 1, 0]]), 35)


if __name__ == '__main__':
    unittest.main()
