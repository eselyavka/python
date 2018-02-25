#!/usr/bin/python

import unittest

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        def is_equal(i, j):
            if i > 0 and j > 0:
                return matrix[i][j] == matrix[i-1][j-1]
            return True

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not is_equal(i, j):
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
