#!/usr/bin/env python

import unittest

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a

        if a[-1] == b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1] == b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'

        return self.addBinary(a[:-1], b[:-1]) + '1'

class TestSolution(unittest.TestCase):
    def test_addBinary(self):
        solution = Solution()
        self.assertEqual(solution.addBinary("1010", "1011"), "10101")
        self.assertEqual(solution.addBinary("11", "1"), "100")

if __name__ == '__main__':
    unittest.main()
