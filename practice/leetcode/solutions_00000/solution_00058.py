#!/usr/bin/env python3

"""LeetCode solution 00058."""

import unittest

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        clean_string = s.strip()

        if not clean_string:
            return 0

        return len(clean_string.split()[-1])

class TestSolution(unittest.TestCase):
    def test_lengthOfLastWord(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord('Hello World'), 5)

if __name__ == '__main__':
    unittest.main()
