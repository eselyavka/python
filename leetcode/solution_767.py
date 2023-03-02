#!/usr/bin/env python

import unittest
import heapq
from collections import defaultdict


class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        freqs = defaultdict(int)

        for c in s:
            freqs[c] -= 1

        h = []
        for c, freq in freqs.items():
            heapq.heappush(h, (freq, c))

        ans = ""
        prev = None

        while h or prev:
            if not h and prev:
                return ""

            freq, c = heapq.heappop(h)
            ans += c
            freq += 1

            if prev:
                heapq.heappush(h, prev)
                prev = None

            if freq != 0:
                prev = (freq, c)

        return ans


class TestSolution(unittest.TestCase):
    def test_reorganizeString(self):
        solution = Solution()
        self.assertEqual(solution.reorganizeString("aaab"), "")
        self.assertEqual(solution.reorganizeString("abbabbaaab"), "ababababab")
        self.assertEqual(solution.reorganizeString("a"), "a")
        self.assertEqual(solution.reorganizeString("aa"), "")
        self.assertEqual(solution.reorganizeString("ab"), "ab")
        self.assertEqual(solution.reorganizeString("aab"), "aba")
        self.assertEqual(solution.reorganizeString("aaab"), "")
        self.assertEqual(solution.reorganizeString("vvvlo"), "vlvov")
        self.assertEqual(solution.reorganizeString("blflxll"), "lblflxl")


if __name__ == '__main__':
    unittest.main()
