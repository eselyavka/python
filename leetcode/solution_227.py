#!/usr/bin/env python

import unittest


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        allowed_ops = set(['+', '-', '*', '/'])
        digit_stack = []

        sign = '+'
        num = 0

        for i, c in enumerate(s):

            if c.isdigit():
                num = num * 10 + int(c)

            if i + 1 == len(s) or c in allowed_ops:
                if sign == '+':
                    digit_stack.append(num)
                elif sign == '-':
                    digit_stack.append(-num)
                elif sign == '*':
                    digit_stack[-1] = digit_stack[-1] * num
                else:
                    digit_stack[-1] = int(digit_stack[-1] / float(num))
                sign = c
                num = 0

        return sum(digit_stack)


class TestSolution(unittest.TestCase):
    def test_calculate(self):
        solution = Solution()

        self.assertEqual(solution.calculate("14-3/2"), 13)


if __name__ == '__main__':
    unittest.main()
