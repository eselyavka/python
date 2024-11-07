#!/usr/bin/env python

import unittest

class Solution(object):
    def left_to_right(self, n):
        if n <= 2:
            return n
        return 2 * self.right_to_left(n//2)

    def right_to_left(self, n):
        if n <= 2:
            return 1
        if n % 2 == 1: return 2 * self.left_to_right(n//2)
        return 2 * self.left_to_right(n//2) - 1

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.left_to_right(n)

class TestSolution(unittest.TestCase):

    def test_lastRemaining(self):
        solution = Solution()
        self.assertEqual(solution.lastRemaining(9), 6)
        self.assertEqual(solution.lastRemaining(10), 8)
        self.assertEqual(solution.lastRemaining(3), 2)
        self.assertEqual(solution.lastRemaining(1), 1)
        self.assertEqual(solution.lastRemaining(2), 2)

if __name__ == '__main__':
    unittest.main()
