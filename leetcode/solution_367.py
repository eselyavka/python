#!/usr/bin/env python

import unittest

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        root = num/2

        for _ in range(20):
            root = 0.5*(root + num/root)

        return root == int(root)

class TestSolution(unittest.TestCase):

    def test_isPerfectSquare(self):
        solution = Solution()
        self.assertTrue(solution.isPerfectSquare(16))
        self.assertFalse(solution.isPerfectSquare(14))
        self.assertFalse(solution.isPerfectSquare(2))
        self.assertTrue(solution.isPerfectSquare(1))

if __name__ == '__main__':
    unittest.main()
