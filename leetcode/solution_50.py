#!/usr/bin/env python

import unittest

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return x

        res, _pow = 1.0, n

        if n < 0:
            _pow, x = -_pow, 1.0/x

        while _pow:
            if _pow & 1:
                res *= x

            x, _pow = x*x, _pow >> 1

        return res

class TestSolution(unittest.TestCase):
    def test_myPow(self):
        solution = Solution()
        self.assertEquals(solution.myPow(2.0, 10), 1024.0)

if __name__ == '__main__':
    unittest.main()
