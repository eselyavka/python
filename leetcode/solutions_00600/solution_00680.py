#!/usr/bin/env python

import unittest

class Solution(object):
    def is_palindrom(self, s, r, l):
        while r < l:
            if s[r] != s[l]:
                return False
            r += 1
            l -= 1

        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True

        right = 0
        left = len(s) - 1
        while right < left:
            if s[right] == s[left]:
                right += 1
                left -= 1
            else:
                if self.is_palindrom(s, right+1, left):
                    return True
                if self.is_palindrom(s, right, left - 1):
                    return True

                return False
        return True

class TestSolution(unittest.TestCase):
    def test_validPalindrome(self):
        solution = Solution()
        self.assertTrue(solution.validPalindrome("aba"))
        self.assertTrue(solution.validPalindrome("abca"))
        self.assertFalse(solution.validPalindrome("abcda"))
        self.assertTrue(solution.validPalindrome(""))
        self.assertTrue(solution.validPalindrome("b"))
        self.assertTrue(solution.validPalindrome("ac"))
        self.assertFalse(solution.validPalindrome("ack"))
        self.assertTrue(solution.validPalindrome("deeee"))
        self.assertTrue(solution.validPalindrome("eeeed"))
        self.assertTrue(solution.validPalindrome("cdbeeeabddddbaeedebdc"))
        self.assertTrue(solution.validPalindrome("ebcbbececabbacecbbcbe"))

if __name__ == '__main__':
    unittest.main()
