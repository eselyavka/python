#!/usr/bin/env python

import unittest


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return x
        if x == 1:
            return 1

        l = 1
        r = x/2 + 1
        while l < r:
            m = r // 2
            if m*m <= x:
                while m*m <= x:
                    m += 1
                return m - 1
            else:
                r = m


class TestSolution(unittest.TestCase):
    def test_mySqrt(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(2), 1)
        self.assertEqual(solution.mySqrt(3), 1)
        self.assertEqual(solution.mySqrt(4), 2)
        self.assertEqual(solution.mySqrt(8), 2)
        self.assertEqual(solution.mySqrt(2147395599), 46339)


if __name__ == '__main__':
    unittest.main()
