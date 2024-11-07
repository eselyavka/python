#!/usr/bin/env python

import unittest


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True

        if len(s) > len(t):
            return False

        i, j = 0, 0

        while i < len(s):
            try:
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            except IndexError:
                return False

        if i != len(s):
            return False

        return True


class TestSolution(unittest.TestCase):
    def test_isSubsequence(self):
        solution = Solution()
        self.assertTrue(solution.isSubsequence("abc", "ahbgdc"))
        self.assertFalse(solution.isSubsequence("axc", "ahbgdc"))
        self.assertTrue(solution.isSubsequence("rrr", "kkkkrrr"))


if __name__ == '__main__':
    unittest.main()
