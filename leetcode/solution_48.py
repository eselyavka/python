#!/usr/bin/env python

import unittest

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        l = row - 1
        for i in range(row/2):
            for j in range(i, (l-i)):
                p1 = matrix[i][j]
                p2 = matrix[j][l-i]
                p3 = matrix[l-i][l-j]
                p4 = matrix[l-j][i]

                matrix[j][l-i], p1 = p1, matrix[j][l-i]
                matrix[l-i][l-j], p2 = p2, matrix[l-i][l-j]
                matrix[l-j][i], p3 = p3, matrix[l-j][i]
                matrix[i][j], p4 = p4, matrix[i][j]

class TestSolution(unittest.TestCase):
    def test_rotate(self):
        _in = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

        solution = Solution()
        solution.rotate(_in)
        self.assertListEqual(_in, [[7, 4, 1],
                                   [8, 5, 2],
                                   [9, 6, 3]])

if __name__ == '__main__':
    unittest.main()
