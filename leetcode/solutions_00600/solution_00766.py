#!/usr/bin/python

import unittest


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if i < n - 1 and j < m - 1:
                    if matrix[i][j] != matrix[i+1][j+1]:
                        return False
        return True


class TestSolution(unittest.TestCase):

    def test_isToeplitzMatrix(self):
        solution = Solution()

        self.assertTrue(solution.isToeplitzMatrix([[1, 2, 3, 4],
                                                   [5, 1, 2, 3],
                                                   [9, 5, 1, 2]]))
        self.assertFalse(solution.isToeplitzMatrix([[1, 2], [2, 2]]))


if __name__ == '__main__':
    unittest.main()
