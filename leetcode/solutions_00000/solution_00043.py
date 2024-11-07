#!/usr/bin/env python

import unittest

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                res[i+j+1] += int(num1[i]) * int(num2[j])
                res[i+j] += res[i+j+1] // 10
                res[i+j+1] %= 10

        res = res[next((i for i, x in enumerate(res) if x != 0), len(res)):]

        return ''.join([str(x) for x in res])

class TestSolution(unittest.TestCase):

    def test_multiply(self):
        solution = Solution()

        self.assertEqual(solution.multiply("2", "3"), "6")
        self.assertEqual(solution.multiply("123", "456"), "56088")

if __name__ == '__main__':
    unittest.main()
