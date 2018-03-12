#!/usr/bin/env python

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
            if d.has_key(c):
                d[c] = float('inf')
            else:
                d[c] = i

        res = sorted(d.values())[0] if sorted(d.values())[0] != float('inf') else -1

        return res

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
