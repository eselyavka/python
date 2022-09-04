#!/usr/bin/env python

import unittest


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s

        if s == s[::-1]:
            return s

        def is_palindrom(s, i, j):
            substr = s[i:j+1]
            return (substr, substr == substr[::-1])

        max_= ""
        for i in range(len(s)):
            for j in range(len(s)-1, i, -1):
                if s[i] == s[j]:
                    res, flag = is_palindrom(s,i,j)
                    if flag and len(max_) < len(res):
                        max_ = res

        return max_ if max_ else s[0]


class TestSolution(unittest.TestCase):
    def test_longestPalindrome(self):
        solution = Solution()

        self.assertEqual(solution.longestPalindrome("babad"), "bab")


if __name__ == '__main__':
    unittest.main()
