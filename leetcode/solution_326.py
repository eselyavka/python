#!/usr/bin/env python

import unittest

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 1.0:
            return True
        elif n < 1.0:
            return False

        return self.isPowerOfThree(float(n)/3.0)

class TestSolution(unittest.TestCase):

    def test_isPowerOfThree(self):

        solution = Solution()
        self.assertTrue(solution.isPowerOfThree(27))
        self.assertFalse(solution.isPowerOfThree(18))

if __name__ == '__main__':
    unittest.main()
