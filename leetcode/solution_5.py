#!/usr/bin/env python

import unittest


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_palindrome(s, left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        n = len(s)
        if n == 1:
            return s

        if s == s[::-1]:
            return s

        max_ = 1
        ans = ""
        for i in range(n):
            for j in range(i+1, n):
                if is_palindrome(s, i, j):
                    if j-i+1 > max_:
                        max_ = j-i+1
                        ans = s[i:j+1]
        return ans if max_ > 1 else s[0]


class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        res = ""
        dp = [None for i in range(n)]

        for j in range(n):
            for i in range(j+1):
                if i == j:
                    dp[i] = True
                elif j == i+1:
                    dp[i] = (s[i] == s[j])
                else:
                    dp[i] = (dp[i+1] and s[i] == s[j])
                if dp[i] and j - i + 1 > len(res):
                    res = s[i:j+1]

        return res


class TestSolution(unittest.TestCase):
    def test_longestPalindrome(self):
        solution = Solution()

        self.assertEqual(solution.longestPalindrome("babad"), "bab")

        solution2 = Solution2()
        self.assertEqual(solution2.longestPalindrome("babad"), "bab")


if __name__ == '__main__':
    unittest.main()
