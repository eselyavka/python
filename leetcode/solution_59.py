#!/usr/bin/env python

import unittest


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]

        row = col = n - 1
        res = [[float('-inf')]*n for _ in range(n)]
        element = 1
        x = y = init_x = init_y = 0

        while True:
            if x >= n or y >= n:
                break

            if res[x][y] == float('-inf'):
                res[x][y] = element

            # right
            while y < col:
                y += 1
                element += 1
                if res[x][y] == float('-inf'):
                    res[x][y] = element

            # down
            while x < row:
                x += 1
                element += 1
                if res[x][y] == float('-inf'):
                    res[x][y] = element

            # left
            while y > init_y:
                y -= 1
                element += 1
                if res[x][y] == float('-inf'):
                    res[x][y] = element
            # up
            while x > init_x:
                x -= 1
                element += 1
                if res[x][y] == float('-inf'):
                    res[x][y] = element

            init_x += 1
            init_y += 1
            x = init_x
            y = init_y
            row -= 1
            col -= 1

        return res


class TestSolution(unittest.TestCase):
    def test_generateMatrix(self):
        solution = Solution()
        self.assertListEqual(solution.generateMatrix(3), [[1, 2, 3],
                                                          [8, 9, 4],
                                                          [7, 6, 5]])


if __name__ == '__main__':
    unittest.main()
