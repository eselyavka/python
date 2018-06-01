#!/usr/bin/python

import unittest

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        mas = []
        def backtrack(s='', l=0, r=0):
            if len(s) == 2 * n:
                mas.append(s)
                return

            if l < n:
                backtrack(s+'(', l+1, r)

            if r < l:
                backtrack(s+')', l, r+1)

        backtrack()
        return mas

class TestSolution(unittest.TestCase):

    def test_generateParenthesis(self):
        solution = Solution()

        self.assertEqual(solution.generateParenthesis(2),
                         ['(())', '()()'])
        self.assertEqual(solution.generateParenthesis(3),
                         ["((()))",
                          "(()())",
                          "(())()",
                          "()(())",
                          "()()()"])

if __name__ == '__main__':
    unittest.main()
