#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == s[::-1]:
            return len(s)

        d = defaultdict(int)

        for c in s:
            d[c] += 1

        _len = 0

        for k in d:
            if d[k] % 2 == 1:
                d[k] -= 1
            _len += d[k]

        return _len + 1 if _len + 1 <= len(s) else _len

class TestSolution(unittest.TestCase):

    def test_longestPalindrome(self):
        solution = Solution()
        self.assertEqual(solution.longestPalindrome('abccccdd'), 7)
        self.assertEqual(solution.longestPalindrome('ccc'), 3)
        self.assertEqual(solution.longestPalindrome('bananas'), 5)

if __name__ == '__main__':
    unittest.main()
