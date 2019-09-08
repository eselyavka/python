#!/usr/bin/env python

import unittest


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if len(str1) > len(str2):
            return self.gcdOfStrings(str2, str1)
        elif str1 == '' or str1 == str2:
            return str1
        elif str2.startswith(str1):
            return self.gcdOfStrings(str1, str2[len(str1):])

        return ''


class TestSolution(unittest.TestCase):

    def test_gcdOfStrings(self):
        solution = Solution()

        self.assertEqual(solution.gcdOfStrings("ABCABC", "ABC"), "ABC")
        self.assertEqual(solution.gcdOfStrings("ABABAB", "ABAB"), "AB")
        self.assertEqual(solution.gcdOfStrings("LEET", "CODE"), "")
        self.assertEqual(solution.gcdOfStrings("AAA", "AA"), "A")
        self.assertEqual(solution.gcdOfStrings("B", "B"), "B")
        self.assertEqual(solution.gcdOfStrings("B", "C"), "")
        self.assertEqual(solution.gcdOfStrings(
            "TAUXXTAUXXTAUXXTAUXXTAUXX",
            "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"), "TAUXX")


if __name__ == '__main__':
    unittest.main()
