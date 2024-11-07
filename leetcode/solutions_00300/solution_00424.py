#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        n = len(s)
        seen = defaultdict(int)
        l, ans = 0, 0

        for r in range(n):
            seen[s[r]] += 1
            while (r - l + 1) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l+=1
            ans = max(ans, r - l + 1)

        return ans

class TestSolution(unittest.TestCase):

    def test_characterReplacement(self):
        solution = Solution()

        self.assertEqual(solution.characterReplacement("ABAB", 2), 4)

if __name__ == '__main__':
    unittest.main()
