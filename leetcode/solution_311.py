#!/usr/bin/env python

import unittest

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 1:
            if len(B) == 1:
                return [[A[0][0] * B[0][0]]]
            return [[A[0][0] * B[0][0] + A[0][1] * B[1][0]]]

        res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

        db = {}

        for i, row in enumerate(B):
            db[i] = {}
            for j, elem in enumerate(row):
                if elem:
                    db[i][j] = elem

        for i, row in enumerate(A):
            for j, elem in enumerate(row):
                for l, elemB in db[j].iteritems():
                    if elem:
                        res[i][l] += elem * elemB
        return res

class TestSolution(unittest.TestCase):
    def test_multiply(self):
        solution = Solution()
        self.assertEquals(solution.multiply(
            [[1, 0, 0],
             [-1, 0, 3]],
            [[7, 0, 0],
             [0, 0, 0],
             [0, 0, 1]]), [[7, 0, 0],
                           [-7, 0, 3]])

        self.assertEquals(solution.multiply([[1, -5]], [[12], [-1]]), [[17]])
        self.assertEquals(solution.multiply([[0]], [[0]]), [[0]])
        self.assertEquals(solution.multiply([[1, 1], [1, 0]], [[1, 0], [1, 0]]),
                          [[2, 0], [1, 0]])
        self.assertEquals(solution.multiply([[0, 1],
                                             [0, 0],
                                             [0, 1]], [[1, 0],
                                                       [1, 0]]), [[1, 0],
                                                                  [0, 0],
                                                                  [1, 0]])


if __name__ == '__main__':
    unittest.main()
