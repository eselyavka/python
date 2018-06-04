#!/usr/bin/env python

import unittest

class Solution(object):
    def _fib(self, n):
        a = 0
        b = 1

        if n == 0:
            return a
        if n == 1:
            return b

        for i in range(2, n+1):
            c = a + b
            a = b
            b = c

        return b

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self._fib(n+1)

class TestSolution(unittest.TestCase):

    def test_climbStairs(self):
        solution = Solution()

        self.assertEqual(solution.climbStairs(2), 2)
        self.assertEqual(solution.climbStairs(3), 3)

if __name__ == '__main__':
    unittest.main()
