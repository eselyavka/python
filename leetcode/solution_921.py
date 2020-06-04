#!/usr/bin/env python

import unittest


class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0

        open_ = []
        unbalanced = 0
        for c in S:
            if c == '(':
                open_.append(c)
            if c == ')':
                try:
                    open_.pop()
                except IndexError:
                    unbalanced += 1

        return unbalanced + len(open_)


class TestSolution(unittest.TestCase):

    def test_minAddToMakeValid(self):
        solution = Solution()
        self.assertEqual(solution.minAddToMakeValid('())'), 1)


if __name__ == '__main__':
    unittest.main()
