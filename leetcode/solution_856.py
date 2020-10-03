#!/usr/bin/env python

import unittest

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = [0]

        for c in S:
            if c == '(':
                stack.append(0)
            else:
                depth = stack.pop()
                stack[-1] += max(2*depth, 1)

        return stack[-1]


class TestSolution(unittest.TestCase):
    def test_scoreOfParentheses(self):
        solution = Solution()
        self.assertEqual(solution.scoreOfParentheses('()'), 1)
        self.assertEqual(solution.scoreOfParentheses('(())'), 2)
        self.assertEqual(solution.scoreOfParentheses('()()'), 2)
        self.assertEqual(solution.scoreOfParentheses('(()(()))'), 6)


if __name__ == '__main__':
    unittest.main()
