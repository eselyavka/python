#!/usr/bin/env python

import unittest

class Solution(object):
    def _rec(self, num, arr):
        if num == 0:
            return int(''.join([str(x) for x in arr[::-1]])) if arr else 0
        rem = abs(num)%7
        arr.append(rem)
        return self._rec(abs(num)/7, arr)

    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        #mas = list()
        #res = self._rec(num, mas) * -1 if num < 0 else self._rec(num, mas)

        return self.convertToAnyBase(num, 7)

    def convertToAnyBase(self, num, base):
        if num == 0:
            return str(num)

        digits = '0123456789ABCDEF'
        stack = []

        res = '-' if num < 0 else ''
        num = abs(num)

        while num > 0:
            rem = num % base
            stack.append(rem)
            num = num // base

        while stack:
            res += digits[stack.pop()]

        return res

class TestSolution(unittest.TestCase):

    def test_convertToBase7(self):
        nums = [100, -7, 0]
        solution = Solution()
        self.assertEqual(solution.convertToBase7(nums[0]), "202")
        self.assertEqual(solution.convertToBase7(nums[1]), "-10")
        self.assertEqual(solution.convertToBase7(nums[2]), "0")

        self.assertEqual(solution.convertToAnyBase(nums[0], 7), "202")
        self.assertEqual(solution.convertToAnyBase(nums[1], 7), "-10")
        self.assertEqual(solution.convertToAnyBase(nums[2], 7), "0")

if __name__ == '__main__':
    unittest.main()
