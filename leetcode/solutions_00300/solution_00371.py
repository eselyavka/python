#!/usr/bin/env python

import unittest

class Solution(object):
    def add(self, a, b):
        mask = 0xFFFFFFFF
        _max = 0x7FFFFFFF

        while b:
            carry = a & b
            a = (a ^ b) & mask
            b = (carry << 1) & mask

        return a if a <= _max else ~(a ^ mask)

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return self.add(a, b)

class TestSolution(unittest.TestCase):
    def test_getSum(self):
        solution = Solution()
        self.assertEqual(solution.getSum(1, 2), 3)
        self.assertEqual(solution.getSum(-2, -3), -5)
        self.assertEqual(solution.getSum(3, -2), 1)
        self.assertEqual(solution.getSum(-14, 16), 2)
        self.assertEqual(solution.getSum(2147483647, -2147483648), -1)

if __name__ == '__main__':
    unittest.main()
