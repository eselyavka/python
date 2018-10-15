#!/usr/bin/env python

import unittest

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        res, rank1 = 0, 10 ** (len(num1) - 1)

        for c1 in num1:
            acc, rank2 = 0, 10 ** (len(num2) - 1)
            for c2 in num2:
                acc += (int(c1) * rank1) * (int(c2) * rank2)
                rank2 = rank2 // 10

            rank1 = rank1 // 10

            res += acc

        return str(res)

class TestSolution(unittest.TestCase):

    def test_multiply(self):
        solution = Solution()

        self.assertEqual(solution.multiply("2", "3"), "6")
        self.assertEqual(solution.multiply("123", "456"), "56088")

if __name__ == '__main__':
    unittest.main()
