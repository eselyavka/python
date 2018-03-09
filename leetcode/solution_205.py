#!/usr/bin/env python

import unittest

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        i = 0
        d = {}
        while i < len(s):
            if d.has_key(s[i]):
                i += 1
                continue
            d[s[i]] = t[i]
            i += 1

        if len(d.keys()) != len(set(d.values())):
            return False

        res = ''
        for c in s:
            res += d[c]

        return res == t

class TestSolution(unittest.TestCase):

    def test_isIsomorphic(self):
        strings = [('egg', 'add'),
                   ('foo', 'bar'),
                   ('paper', 'title'),
                   ('aba', 'baa'),
                   ('abba', 'abab'),
                   ('ab', 'aa')]
        solution = Solution()
        self.assertTrue(solution.isIsomorphic(*strings[0]))
        self.assertFalse(solution.isIsomorphic(*strings[1]))
        self.assertTrue(solution.isIsomorphic(*strings[2]))
        self.assertFalse(solution.isIsomorphic(*strings[3]))
        self.assertFalse(solution.isIsomorphic(*strings[4]))
        self.assertFalse(solution.isIsomorphic(*strings[5]))

if __name__ == '__main__':
    unittest.main()
