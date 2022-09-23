#!/usr/bin/env python

import unittest
from collections import Counter

class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        if not order:
            return s

        frequencies = Counter(s)

        res = ""
        for c in order:
            freq = frequencies.get(c)
            if freq is not None:
                res += c * freq
                frequencies.pop(c)

        leftovers = "".join([c * frequencies[c] for c in frequencies])

        return res + leftovers


class TestSolution(unittest.TestCase):

    def test_customSortString(self):
        solution = Solution()
        self.assertEqual(solution.customSortString("cba", "abcd"), "cbad")
        self.assertEqual(solution.customSortString("", "abcd"), "abcd")
        self.assertEqual(solution.customSortString("a", "bcdaa"), "aabcd")
        self.assertEqual(solution.customSortString("ab", "bcdaa"), "aabcd")
        self.assertEqual(solution.customSortString("kqep", "pekeq"), "kqeep")


if __name__ == '__main__':
    unittest.main()
