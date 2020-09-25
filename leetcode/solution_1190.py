#!/usr/bin/env python

import unittest


class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        start = []
        res = s
        for i, c in enumerate(s):
            if c == ')':
                b = start.pop()
                res = res[:b+1] + res[i-1:b:-1] + res[i:]
            elif c == '(':
                start.append(i)

        return res.replace('(', '').replace(')', '')


class TestSolution(unittest.TestCase):
    def test_reverseParentheses(self):
        solution = Solution()
        self.assertEqual(solution.reverseParentheses("(u(love)i)"), "iloveu")


if __name__ == '__main__':
    unittest.main()
