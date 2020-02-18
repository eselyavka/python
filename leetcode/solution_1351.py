#!/usr/bin/env python

import unittest


class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] < 0:
                    res += 1
                else:
                    break

        return res


class TestSolution(unittest.TestCase):

    def test_countNegatives(self):
        solution = Solution()
        self.assertEqual(solution.countNegatives([[1, -1], [-1, -1]]), 3)


if __name__ == '__main__':
    unittest.main()
