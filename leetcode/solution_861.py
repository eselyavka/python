#!/usr/bin/env python

import unittest
import math


class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        m = len(A[0])

        for i in range(n):
            if A[i][0] == 0:
                for j in range(m):
                    A[i][j] = -A[i][j] + 1

        for j in range(1, m):
            count_zero = 0
            for i in range(n):
                if not A[i][j]:
                    count_zero += 1
            if count_zero >= math.ceil(float(n) / 2.0):
                for i in range(n):
                    A[i][j] = -A[i][j] + 1

        res = 0
        for i in range(n):
            buf = []
            for j in range(m):
                buf.append(str(A[i][j]))
            res += int(''.join(buf), 2)

        return res


class TestSolution(unittest.TestCase):
    def test_matrixScore(self):
        solution = Solution()
        self.assertEqual(solution.matrixScore([[1, 1], [1, 1], [0, 1]]), 8)


if __name__ == '__main__':
    unittest.main()
