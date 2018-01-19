#!/usr/bin/env python

import unittest

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 9
        elif n == 2:
            return 987

        for a in xrange(2, 9*pow(10, (n-1))):
            upper = pow(10, n) - a
            lower = int(str(upper)[::-1])

            D = pow(a, 2)-4*lower

            if D < 0:
                continue

            if pow(D, .5) == int(pow(D, .5)):
                return (lower+pow(10, n)*(pow(10, n)-a)) % 1337

class TestSolution(unittest.TestCase):

    def test_largestPalindrome(self):
        solution = Solution()
        self.assertEqual(solution.largestPalindrome(1), 9)
        self.assertEqual(solution.largestPalindrome(2), 987)
        self.assertEqual(solution.largestPalindrome(3), 123)

if __name__ == '__main__':
    unittest.main()
