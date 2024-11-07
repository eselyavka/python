#!/usr/bin/env python

import unittest


class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        d = {}

        def rec(n):
            if n < 0:
                return

            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1

            if n in d:
                return d[n]

            result = rec(n-1) + rec(n - 2) + rec(n - 3)
            d[n] = result

            return result

        return rec(n)


class TestSolution(unittest.TestCase):
    def test_tribonacci(self):
        solution = Solution()
        self.assertEqual(solution.tribonacci(25), 1389537)


if __name__ == '__main__':
    unittest.main()
