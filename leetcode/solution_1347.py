#!/usr/bin/env python

import unittest
from collections import Counter


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) != len(t):
            return 0

        if s == t:
            return 0

        c_s = Counter(s)
        c_t = Counter(t)

        res = 0
        for c in t:
            if c_s.get(c):
                if c_t[c] > c_s[c]:
                    res += abs(c_s[c] - c_t[c])
                    c_s[c] += res
            else:
                res += 1

        return res


class TestSolution(unittest.TestCase):

    def test_minSteps(self):
        solution = Solution()
        self.assertEqual(solution.minSteps("bab", "aba"), 1)


if __name__ == '__main__':
    unittest.main()
