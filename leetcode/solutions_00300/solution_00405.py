#!/usr/bin/env python

import unittest

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        digits = '0123456789abcdef'
        stack = []

        base = 16

        max_int = 4294967295

        if num < 0:
            num = max_int - (abs(num) - 1)

        while num > 0:
            rem = num % base
            stack.append(rem)
            num = num // base

        res = ''
        while stack:
            res += digits[stack.pop()]

        return res

class TestSolution(unittest.TestCase):

    def test_toHex(self):
        nums = [26, -1, -2]
        solution = Solution()
        self.assertEqual(solution.toHex(0), "0")
        self.assertEqual(solution.toHex(nums[0]), "1a")
        self.assertEqual(solution.toHex(nums[1]), "ffffffff")
        self.assertEqual(solution.toHex(nums[2]), "fffffffe")

if __name__ == '__main__':
    unittest.main()
