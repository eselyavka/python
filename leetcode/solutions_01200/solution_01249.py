#!/usr/bin/env python

import unittest


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        open_par, close_par = [], []

        i = 0
        arr_s = list(s)
        while i < len(arr_s):
            if arr_s[i] == '(':
                open_par.append(arr_s[i])
            if arr_s[i] == ')':
                close_par.append(arr_s[i])
                if len(close_par) > len(open_par):
                    arr_s[i] = ''
                    close_par.pop()
            i += 1

        open_par, close_par = [], []
        i = len(arr_s) - 1
        while i >= 0:
            if arr_s[i] == ')':
                close_par.append(arr_s[i])
            if arr_s[i] == '(':
                open_par.append(arr_s[i])
                if len(open_par) > len(close_par):
                    open_par.pop()
                    arr_s[i] = ''
            i -= 1

        return ''.join(arr_s)


class TestSolution(unittest.TestCase):
    def test_minRemoveToMakeValid(self):
        solution = Solution()
        self.assertEqual(
            solution.minRemoveToMakeValid("lee(t(c)o)de)"),
            "lee(t(c)o)de")


if __name__ == '__main__':
    unittest.main()
