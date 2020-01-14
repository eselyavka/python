#!/usr/bin/env python

import unittest


class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N % 2 == 0


class TestSolution(unittest.TestCase):
    def test_divisorGame(self):
        solution = Solution()
        self.assertTrue(solution.divisorGame(2))
        self.assertFalse(solution.divisorGame(3))


if __name__ == '__main__':
    unittest.main()
