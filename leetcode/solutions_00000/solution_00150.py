#!/usr/bin/env python

import unittest


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = {'+': lambda y, x: x + y,
                      '-': lambda y, x: x - y,
                      '*': lambda y, x: x * y,
                      '/': lambda y, x: int(float(x) / float(y))}
        stack = []

        for token in tokens:
            op_ = operations.get(token)
            if op_:
                res = op_(stack.pop(), stack.pop())
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[-1]


class TestSolution(unittest.TestCase):
    def test_evalRPN(self):
        solution = Solution()
        self.assertEqual(solution.evalRPN(['2', '1', '+', '3', '*']), 9)


if __name__ == '__main__':
    unittest.main()
