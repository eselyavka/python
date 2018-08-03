#!/usr/bin/env python

import unittest

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        try:
            return haystack.index(needle)
        except ValueError:
            return -1

class TestSolution(unittest.TestCase):
    def test_strStr(self):
        solution = Solution()
        self.assertEqual(solution.strStr("hello", "ll"), 2)
        self.assertEqual(solution.strStr("aaaaa", "bba"), -1)

if __name__ == '__main__':
    unittest.main()
