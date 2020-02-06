#!/usr/bin/env python

import unittest


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        open_par = []
        close_par = []

        arr = list(s)

        i = 0
        while i < len(arr):
            if arr[i] == '(':
                open_par.append(arr[i])
            if arr[i] == ')':
                close_par.append(arr[i])
                if len(close_par) > len(open_par):
                    arr[i] = ''
                    close_par.pop()
            i += 1

        open_par = []
        close_par = []
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == ')':
                close_par.append(arr[i])
            if arr[i] == '(':
                open_par.append(arr[i])
                if len(open_par) > len(close_par):
                    arr[i] = ''
                    open_par.pop()

        return ''.join(arr)


class TestSolution(unittest.TestCase):
    def test_minRemoveToMakeValid(self):
        solution = Solution()
        self.assertEqual(
            solution.minRemoveToMakeValid("lee(t(c)o)de)"),
            "lee(t(c)o)de")


if __name__ == '__main__':
    unittest.main()
