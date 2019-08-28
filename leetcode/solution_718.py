#!/usr/bin/env python

import unittest


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m = len(A)
        n = len(B)

        matrix = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    matrix[i][j] = matrix[i-1][j-1] + 1

        return max([max(row) for row in matrix])


class TestSolution(unittest.TestCase):
    def test_findLength(self):
        solution = Solution()
        self.assertEqual(solution.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]), 3)
        self.assertEqual(solution.findLength([1], [1]), 1)
        self.assertEqual(solution.findLength([6, 3, 7], [1, 3, 2]), 1)
        self.assertEqual(solution.findLength([1, 2, 2, 3], [4, 2, 2, 6]), 2)
        self.assertEqual(solution.findLength([1, 2, 2, 3, 5, 6, 7], [4, 2, 2, 6, 5, 6, 7]), 3)
        self.assertEqual(solution.findLength([1, 2, 2, 3, 5, 6, 7, 8],
                                             [4, 2, 2, 6, 5, 6, 7, 10]), 3)
        self.assertEqual(solution.findLength([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]), 4)


if __name__ == '__main__':
    unittest.main()
