#!/usr/bin/env python

import unittest

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num // 10 == 0:
            return num

        return self.addDigits(num // 10 + num % 10)

class TestSolution(unittest.TestCase):

    def test_addDigits(self):
        digit = 38
        digit1 = 0

        solution = Solution()
        self.assertEqual(solution.addDigits(digit), 2)
        self.assertFalse(solution.addDigits(digit1), 0)

if __name__ == '__main__':
    unittest.main()
