#!/usr/bin/env python

import unittest


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def rec(matrix, res, init_x, init_y, row, col):
            if init_x > len(matrix)-1 or init_y > len(matrix[0])-1:
                return

            x = init_x
            y = init_y

            if matrix[x][y] != float('-inf'):
                res.append(matrix[x][y])

            matrix[x][y] = float('-inf')

            # left
            while y < col:
                y += 1
                if matrix[x][y] != float('-inf'):
                    res.append(matrix[x][y])
                    matrix[x][y] = float('-inf')

            # down
            while x < row:
                x += 1
                if matrix[x][y] != float('-inf'):
                    res.append(matrix[x][y])
                    matrix[x][y] = float('-inf')

            # right
            while y > init_y:
                y -= 1
                if matrix[x][y] != float('-inf'):
                    res.append(matrix[x][y])
                    matrix[x][y] = float('-inf')

            # up
            while x > init_x:
                x -= 1
                if matrix[x][y] != float('-inf'):
                    res.append(matrix[x][y])
                    matrix[x][y] = float('-inf')

            rec(matrix, res, init_x+1, init_y+1, row-1, col-1)

        if not matrix:
            return []

        res = []

        rec(matrix, res, 0, 0, len(matrix)-1, len(matrix[0])-1)

        return res


class TestSolution(unittest.TestCase):
    def test_spiralOrder(self):
        solution = Solution()
        self.assertListEqual(solution.spiralOrder([[1, 2, 3],
                                                   [4, 5, 6],
                                                   [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])


if __name__ == '__main__':
    unittest.main()
