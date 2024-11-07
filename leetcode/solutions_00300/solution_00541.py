#!/usr/bin/env python

import unittest

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) < k:
            return s[::-1]

        if len(s) >= k and len(s) < 2*k:
            return s[k-1::-1] + s[k:]

        res = ''
        i = 0

        while i < len(s):
            res += (s[(k-1)+i::-1] if i == 0 else s[(k-1)+i:i-1:-1]) + s[k+i:2*k+i]
            i += 2*k

        return res

class TestSolution(unittest.TestCase):
    def test_reverseStr(self):
        solution = Solution()
        self.assertEqual(solution.reverseStr('abc', 10), 'cba')
        self.assertEqual(solution.reverseStr('abc', 2), 'bac')
        self.assertEqual(solution.reverseStr('abcdefj', 2), 'bacdfej')
        self.assertEqual(solution.reverseStr('abcdefjiko', 3), 'cbadefkijo')

if __name__ == '__main__':
    unittest.main()
