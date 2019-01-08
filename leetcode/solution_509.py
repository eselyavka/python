#!/usr/bin/env python

import unittest

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        elif N == 1:
            return 1

        return self.fib(N-1) + self.fib(N-2)


class TestSolution(unittest.TestCase):
    def test_fib(self):
        solution = Solution()
        self.assertEqual(solution.fib(2), 1)
        self.assertEqual(solution.fib(3), 2)
        self.assertEqual(solution.fib(4), 3)


if __name__ == '__main__':
    unittest.main()
