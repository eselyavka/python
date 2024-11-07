#!/usr/bin/env python

import unittest


class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        matrix = []

        for _ in range(d+1):
            new_arr = []
            for _ in range(target+1):
                new_arr.append(-1)
            matrix.append(new_arr)

        def rec(d, t):
            if d == 0 and t == 0:
                return 1
            if d == 0:
                return 0
            if t <= 0:
                return 0

            if matrix[d][t] == -1:
                matrix[d][t] = 0
                for k in range(1, f+1):
                    matrix[d][t] += rec(d-1, t-k)
                    matrix[d][t] %= (1e9 + 7)

            return matrix[d][t]

        rec(d, target)

        return int(matrix[d][target])


class TestSolution(unittest.TestCase):

    def test_numRollsToTarget(self):
        solution = Solution()

        self.assertEqual(solution.numRollsToTarget(1, 6, 3), 1)
        self.assertEqual(solution.numRollsToTarget(2, 6, 7), 6)


if __name__ == '__main__':
    unittest.main()
