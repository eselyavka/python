#!/usr/bin/env python

import unittest

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x is None:
            return False

        if x == 0:
            return True

        if x < 0:
            return False

        if x < 10:
            return True

        s = []

        def break_digit(x):
            if x < 10:
                s.append(x)
                return

            s.append(x % 10)

            break_digit(x//10)

        break_digit(x)
        res = 0
        i = len(s) - 1

        for num in s:
            res += num*pow(10, i)
            i -= 1

        return res == x

class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
        solution = Solution()
        self.assertTrue(solution.isPalindrome(11))
        self.assertTrue(solution.isPalindrome(121))
        self.assertFalse(solution.isPalindrome(-121))
        self.assertFalse(solution.isPalindrome(10))

if __name__ == '__main__':
    unittest.main()
