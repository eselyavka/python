#!/usr/bin/env python

import unittest

class Solution(object):
    def is_overflow(self, x):
        return x > 2147483647 or x < -2147483648

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if self.is_overflow(x):
            return 0

        rev = int(str(abs(x))[::-1]) if x >= 0 else int(str(abs(x))[::-1]) * -1

        if self.is_overflow(rev):
            return 0

        return rev


class TestSolution(unittest.TestCase):

    def test_reverse(self):
        solution = Solution()
        self.assertEqual(solution.reverse(123), 321)
        self.assertEqual(solution.reverse(-123), -321)
        self.assertEqual(solution.reverse(120), 21)

if __name__ == '__main__':
    unittest.main()
