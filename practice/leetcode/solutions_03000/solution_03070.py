#!/usr/bin/env python3

"""LeetCode solution 03070."""

import unittest


class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        prefix = [[0] * cols for _ in range(rows)]
        ans = 0

        for row in range(rows):
            for col in range(cols):
                prefix[row][col] = grid[row][col]
                if row > 0:
                    prefix[row][col] += prefix[row - 1][col]
                if col > 0:
                    prefix[row][col] += prefix[row][col - 1]
                if row > 0 and col > 0:
                    prefix[row][col] -= prefix[row - 1][col - 1]

                if prefix[row][col] <= k:
                    ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_countSubmatrices(self):
        solution = Solution()
        self.assertEqual(solution.countSubmatrices([[7, 6, 3], [6, 6, 1]], 18), 4)
        self.assertEqual(solution.countSubmatrices([[1, 1], [1, 1]], 3), 3)


if __name__ == '__main__':
    unittest.main()
