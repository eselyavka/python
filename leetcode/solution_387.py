#!/usr/bin/env python

from collections import Counter
import unittest


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        d = {}

        for i, c in enumerate(s):
            if c in d:
                d[c] = float('inf')
            else:
                d[c] = i

        res = sorted(d.values())[0] if sorted(d.values())[0] != float('inf') else -1

        return res

    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = Counter(s)

        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i

        return -1


class TestSolution(unittest.TestCase):

    def test_firstUniqChar(self):
        s1 = 'leetcode'
        s2 = 'loveleetcode'
        s3 = ''
        solution = Solution()
        self.assertEqual(solution.firstUniqChar(s1), 0)
        self.assertEqual(solution.firstUniqChar(s2), 2)
        self.assertEqual(solution.firstUniqChar(s3), -1)

        self.assertEqual(solution.firstUniqChar2(s1), 0)
        self.assertEqual(solution.firstUniqChar2(s2), 2)
        self.assertEqual(solution.firstUniqChar2(s3), -1)


if __name__ == '__main__':
    unittest.main()
