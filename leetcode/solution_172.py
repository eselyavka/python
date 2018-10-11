#!/usr/bin/env python

import unittest

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def rec(n):
            if not n:
                return 0

            return n / 5 + rec(n // 5)

        return rec(n)

class TestSolution(unittest.TestCase):

    def test_trailingZeroes(self):
        solution = Solution()

        self.assertEqual(solution.trailingZeroes(3), 0)
        self.assertEqual(solution.trailingZeroes(5), 1)
        self.assertEqual(solution.trailingZeroes(10), 2)
        self.assertEqual(solution.trailingZeroes(8), 1)
        self.assertEqual(solution.trailingZeroes(7), 1)

if __name__ == '__main__':
    unittest.main()
