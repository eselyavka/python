#!/usr/bin/env python

import unittest

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return not n % 4 == 0


class TestSolution(unittest.TestCase):

    def test_canWinNim(self):
        digits = [1, 4, 7, 2, 5]
        solution = Solution()
        self.assertTrue(solution.canWinNim(digits[0]))
        self.assertFalse(solution.canWinNim(digits[1]))
        self.assertTrue(solution.canWinNim(digits[2]))
        self.assertTrue(solution.canWinNim(digits[3]))
        self.assertTrue(solution.canWinNim(digits[4]))

if __name__ == '__main__':
    unittest.main()
