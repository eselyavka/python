#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        if not S:
            return T

        dT = defaultdict(int)

        for c in T:
            dT[c] += 1

        res = ''
        for c in S:
            res += c * dT[c]
            dT[c] = 0

        return res + ''.join([key * dT[key] for key in dT])

class TestSolution(unittest.TestCase):

    def test_customSortString(self):
        solution = Solution()
        self.assertEqual(solution.customSortString("cba", "abcd"), "cbad")
        self.assertEqual(solution.customSortString("", "abcd"), "abcd")
        self.assertEqual(solution.customSortString("a", "bcdaa"), "aacbd")
        self.assertEqual(solution.customSortString("ab", "bcdaa"), "aabcd")
        self.assertEqual(solution.customSortString("kqep", "pekeq"), "kqeep")

if __name__ == '__main__':
    unittest.main()
