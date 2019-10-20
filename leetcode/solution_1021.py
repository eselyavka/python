#!/usr/bin/env python

import unittest


class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        s_open, s_close, stack = [], [], []
        res = ''
        for char in S:
            stack.append(char)
            if char == ')':
                s_close.append(char)
                if len(s_close) == len(s_open):
                    stack.pop()
                    res += ''.join(stack[1:])
                    s_close, s_open, stack = [], [], []
            else:
                s_open.append(char)

        return res


class TestSolution(unittest.TestCase):

    def test_removeOuterParentheses(self):
        solution = Solution()
        self.assertEqual(solution.removeOuterParentheses('(()())(())'), '()()()')
        self.assertEqual(solution.removeOuterParentheses('(()())(())(()(()))'), '()()()()(())')
        self.assertEqual(solution.removeOuterParentheses('()()'), '')


if __name__ == '__main__':
    unittest.main()
