#!/usr/bin/env python

import unittest

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups = []
        rep = 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                rep += 1
            else:
                groups.append(rep)
                rep = 1

        groups.append(rep)
        res = 0

        for i in range(1, len(groups)):
            res += min(groups[i-1], groups[i])
        return res

class TestSolution(unittest.TestCase):

    def test_countBinarySubstrings(self):
        solution = Solution()

        self.assertEqual(solution.countBinarySubstrings("00110011"), 6)
        self.assertEqual(solution.countBinarySubstrings("10101"), 4)
        self.assertEqual(solution.countBinarySubstrings("00110"), 3)

if __name__ == '__main__':
    unittest.main()
