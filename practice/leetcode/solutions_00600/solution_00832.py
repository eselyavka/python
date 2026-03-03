#!/usr/bin/env python3

"""LeetCode solution 00832."""

import unittest

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(A) == 1:
            return [[0 if x else 1 for x in A[0][::-1]]]

        res = [[0 for _ in row] for row in A]

        for i, row in enumerate(A):
            l = len(row)-1
            for j in range(l, -1, -1):
                res[i][l-j] = 0 if row[j] else 1

        return res

class TestSolution(unittest.TestCase):
    def test_flipAndInvertImage(self):
        solution = Solution()
        self.assertEqual(solution.flipAndInvertImage([[1, 1, 0],
                                                      [1, 0, 1],
                                                      [0, 0, 0]]),
                         [[1, 0, 0],
                          [0, 1, 0],
                          [1, 1, 1]])
        self.assertEqual(solution.flipAndInvertImage([[1, 1, 0]]), [[1, 0, 0]])
        self.assertEqual(solution.flipAndInvertImage([[1]]), [[0]])
        self.assertEqual(solution.flipAndInvertImage([[1, 1], [1, 1]]),
                         [[0, 0], [0, 0]])

if __name__ == '__main__':
    unittest.main()
