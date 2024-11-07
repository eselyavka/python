#!/usr/bin/env python

import unittest

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c in [0, 1, 2]:
            return True

        for i in range(int(round(c ** 0.5))):
            calc = (c - i**2) ** 0.5
            if calc == int(calc):
                return True

        return False

class TestSolution(unittest.TestCase):

    def test_judgeSquareSum(self):
        in1 = 5
        in2 = 3
        in3 = 1
        in4 = 2
        in5 = 8
        in6 = 0
        solution = Solution()
        self.assertTrue(solution.judgeSquareSum(in1))
        self.assertTrue(solution.judgeSquareSum(in4))
        self.assertTrue(solution.judgeSquareSum(in5))
        self.assertTrue(solution.judgeSquareSum(in6))
        self.assertTrue(solution.judgeSquareSum(in3))
        self.assertFalse(solution.judgeSquareSum(in2))

if __name__ == '__main__':
    unittest.main()
