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

        i = len(s) - 1
        j = len(t) - 1

        while i > -1:
            if s[i] == t[j]:
                i -= 1
                j -= 1
            else:
                if j > -1:
                    j -= 1
                else:
                    return False

        if i > 0:
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
