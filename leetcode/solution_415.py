#!/usr/bin/env python

import unittest

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        d = {len(num1) - i:pow(10, i - 1) for i in range(len(num1), 0, -1)}
        d2 = {len(num2) - i:pow(10, i - 1) for i in range(len(num2), 0, -1)}

        res = 0

        for i, c in enumerate(num1):
            res += d[i] * int(c)

        for i, c in enumerate(num2):
            res += d2[i] * int(c)

        return str(res)

class TestSolution(unittest.TestCase):

    def test_addStrings(self):
        solution = Solution()
        self.assertEqual(solution.addStrings('124', '34'), '158')

if __name__ == '__main__':
    unittest.main()
