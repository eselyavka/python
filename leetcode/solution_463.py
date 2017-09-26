#!/usr/bin/env python

import unittest

class Solution(object):
    def _border_checker(self, element):
        return element != 1

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i == 0:
                        count += 1
                    if i == len(grid) - 1:
                        count += 1

                    if i != len(grid) - 1 and self._border_checker(grid[i+1][j]):
                        count += 1
                    if i != 0 and self._border_checker(grid[i-1][j]):
                        count += 1

                    if j == 0:
                        count += 1
                    if j == len(grid[i]) - 1:
                        count += 1

                    if j != len(grid[i]) - 1 and self._border_checker(grid[i][j+1]):
                        count += 1
                    if j != 0 and self._border_checker(grid[i][j-1]):
                        count += 1
        return count

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.grid = [[0, 1, 0, 0],
                     [1, 1, 1, 0],
                     [0, 1, 0, 0],
                     [1, 1, 0, 0]]
        self.one = [[1]]
        self.two = [[1,1]]

    def test_matrixReshape(self):
        solution = Solution()
        self.assertEqual(solution.islandPerimeter(self.grid), 16)
        self.assertEqual(solution.islandPerimeter(self.one), 4)
        self.assertEqual(solution.islandPerimeter(self.two), 6)

if __name__ == '__main__':
    unittest.main()
