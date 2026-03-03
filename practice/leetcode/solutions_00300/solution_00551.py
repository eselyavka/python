#!/usr/bin/env python3

"""LeetCode solution 00551."""

import unittest

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent = 0

        for i, char in enumerate(s):
            if char == 'A':
                absent += 1

            if absent > 1:
                return False

            if i >= 2 and char == s[i-1] == s[i-2] == 'L':
                return False

        return True

class TestSolution(unittest.TestCase):
    def test_checkRecord(self):
        solution = Solution()
        self.assertTrue(solution.checkRecord("PPALLP"))
        self.assertFalse(solution.checkRecord("PPALLL"))
        self.assertTrue(solution.checkRecord("PPALLPLLPPPPLLP"))

if __name__ == '__main__':
    unittest.main()
