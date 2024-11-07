#!/usr/bin/env python

import unittest

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        if num == 0:
            return False

        def devide(num1, num2):
            while num1 % num2 == 0:
                num1 /= num2
            return num1

        num = devide(num, 2)
        num = devide(num, 3)
        num = devide(num, 5)

        return num == 1

class TestSolution(unittest.TestCase):
    def test_isUgly(self):
        solution = Solution()
        self.assertTrue(solution.isUgly(6))
        self.assertTrue(solution.isUgly(8))
        self.assertFalse(solution.isUgly(14))
        self.assertTrue(solution.isUgly(1))
        self.assertFalse(solution.isUgly(0))
        self.assertTrue(solution.isUgly(2))

if __name__ == '__main__':
    unittest.main()
