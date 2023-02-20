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
                backtrack(s + '(', l + 1, r)

            if r < l:
                backtrack(s + ')', l, r + 1)

        backtrack()
        return mas


class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def rec(curr_idx, m, balance, buf, ans):
            if curr_idx == m:
                if balance == 0:
                    ans.append("".join(buf))
                return
            if balance > 0:
                buf[curr_idx] = ")"
                rec(curr_idx + 1, m, balance - 1, buf, ans)

            buf[curr_idx] = "("
            rec(curr_idx + 1, m, balance + 1, buf, ans)

        buf = [None] * (2 * n)
        rec(0, 2 * n, 0, buf, ans)

        return ans


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

        solution2 = Solution2()
        self.assertEqual(sorted(solution2.generateParenthesis(2)),
                         sorted(['(())', '()()']))
        self.assertEqual(sorted(solution2.generateParenthesis(3)),
                         sorted(["((()))",
                                 "(()())",
                                 "(())()",
                                 "()(())",
                                 "()()()"]))


if __name__ == '__main__':
    unittest.main()
