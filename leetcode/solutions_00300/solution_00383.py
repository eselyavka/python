#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = defaultdict(int)

        for c in magazine:
            d[c] += 1

        for c in ransomNote:
            if c not in d:
                return False
            if not d[c]:
                return False
            d[c] -= 1

        return True

class TestSolution(unittest.TestCase):

    def test_canConstruct(self):

        solution = Solution()

        self.assertTrue(solution.canConstruct("aa", "aab"))
        self.assertFalse(solution.canConstruct("aa", "ab"))
        self.assertFalse(solution.canConstruct("a", "b"))

if __name__ == '__main__':
    unittest.main()
