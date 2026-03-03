#!/usr/bin/env python3

"""LeetCode solution 00389."""

import unittest
from collections import defaultdict

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = defaultdict(int)

        for c in t:
            d[c] += 1

        for c in s:
            if c in d:
                d[c] -= 1

        return ''.join([x[0] for x in d.items() if x[1] > 0])

class TestSolution(unittest.TestCase):
    def test_findTheDifference(self):
        solution = Solution()
        self.assertEqual(solution.findTheDifference('abcd', 'abcde'), 'e')

if __name__ == '__main__':
    unittest.main()
