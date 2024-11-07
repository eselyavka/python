#!/usr/bin/env python

import unittest

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(A[0])

        if row == col:
            AT = [[0 for _ in range(col)] for _ in range(row)]
        else:
            AT = [[0 for _ in range(row)] for _ in range(col)]

        for i in range(row):
            for j in range(col):
                if i == j:
                    AT[i][j] = A[i][j]
                else:
                    AT[j][i] = A[i][j]

        return AT

class TestSolution(unittest.TestCase):
    def test_transpose(self):
        solution = Solution()
        self.assertListEqual(solution.transpose([[1, 2, 3],
                                                 [4, 5, 6],
                                                 [7, 8, 9]]),
                             [[1, 4, 7],
                              [2, 5, 8],
                              [3, 6, 9]])
        self.assertListEqual(solution.transpose([[1, 2, 3],
                                                 [4, 5, 6]]),
                             [[1, 4],
                              [2, 5],
                              [3, 6]])

if __name__ == '__main__':
    unittest.main()
