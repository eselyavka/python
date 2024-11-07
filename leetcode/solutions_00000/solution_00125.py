#!/usr/bin/env python

import unittest

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        r = 0
        l = len(s) - 1

        while r < len(s) and l > -1:
            if not s[r].isalnum():
                r += 1
                continue

            if not s[l].isalnum():
                l -= 1
                continue

            if s[r].lower() != s[l].lower():
                return False

            r += 1
            l -= 1

        return True

class TestSolution(unittest.TestCase):

    def test_isPalindrome(self):
        solution = Solution()
        self.assertTrue(solution.isPalindrome('A man, a plan, a canal: Panama'))
        self.assertFalse(solution.isPalindrome('race a car'))
        self.assertTrue(solution.isPalindrome(''))
        self.assertTrue(solution.isPalindrome('a'))
        self.assertTrue(solution.isPalindrome('a.'))
        self.assertFalse(solution.isPalindrome('0P'))

if __name__ == '__main__':
    unittest.main()
