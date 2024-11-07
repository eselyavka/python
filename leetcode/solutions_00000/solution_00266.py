#!/usr/bin/env python

import unittest

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = dict()

        if s == s[::-1]:
            return True

        for letter in s:
            if d.has_key(letter):
                d[letter] += 1
            else:
                d[letter] = 1

        cnt = 0

        for k in d:
            if d[k] % 2 == 1:
                cnt += 1

        return not cnt > 1

class TestSolution(unittest.TestCase):

    def test_canPermutePalindrome(self):
        solution = Solution()
        strings = ["code", "aab", "carerac", "aabb"]
        self.assertFalse(solution.canPermutePalindrome(strings[0]))
        self.assertTrue(all([solution.canPermutePalindrome(s) for s in strings[1:]]))

if __name__ == '__main__':
    unittest.main()
