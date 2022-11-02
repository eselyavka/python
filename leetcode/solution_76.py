#!/usr/bin/env python

import unittest
from collections import Counter, defaultdict


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtyp
        e: str
        """
        if len(t) > len(s):
            return ""

        mapping = Counter(t)
        seen = defaultdict(int)
        l, cnt = 0, 0
        n = len(t)
        ans = float("inf"), None, None

        for i, c in enumerate(s):
            seen[c] += 1

            if c in mapping and seen[c] <= mapping[c]:
                cnt+=1
            r = i
            while l <= r and cnt == n:
                ch = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                seen[ch] -= 1
                if ch in mapping and seen[ch] < mapping[ch]:
                    cnt -= 1
                l += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]


class TestSolution(unittest.TestCase):

    def test_minWindow(self):
        solution = Solution()

        self.assertEqual(solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")


if __name__ == '__main__':
    unittest.main()
