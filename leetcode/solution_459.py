#!/usr/bin/env python

import unittest

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        for i in range(1, len(s)):
            _s = s[:i]
            if _s * (((len(s) - len(_s))/len(_s))+1) == s:
                return True

        return False

class TestSolution(unittest.TestCase):
    def test_repeatedSubstringPattern(self):
        solution = Solution()
        self.assertTrue(solution.repeatedSubstringPattern("abab"))
        self.assertFalse(solution.repeatedSubstringPattern("aba"))
        self.assertTrue(solution.repeatedSubstringPattern("abcabcabcabc"))

if __name__ == '__main__':
    unittest.main()
