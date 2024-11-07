#!/usr/bin/env python

import unittest
from collections import defaultdict
from string import ascii_lowercase


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        freq = defaultdict(int)
        idx = defaultdict(int)
        for i in range(n):
            freq[s[i]] += 1
            idx[s[i]] = i

        ans = n

        for c in ascii_lowercase:
            if freq.get(c) == 1:
                ans = min(ans, idx.get(c, n))

        return -1 if ans == n else ans


class TestSolution(unittest.TestCase):

    def test_firstUniqChar(self):
        s1 = 'leetcode'
        s2 = 'loveleetcode'
        s3 = ''
        solution = Solution()
        self.assertEqual(solution.firstUniqChar(s1), 0)
        self.assertEqual(solution.firstUniqChar(s2), 2)
        self.assertEqual(solution.firstUniqChar(s3), -1)


if __name__ == '__main__':
    unittest.main()
