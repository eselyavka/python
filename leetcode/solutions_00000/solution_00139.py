#!/usr/bin/env python

import unittest


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n + 1)

        dp[n] = True
        for i in range(n - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


class TestSolution(unittest.TestCase):

    def test_wordBreak(self):
        solution = Solution()

        self.assertTrue(solution.wordBreak('leetcode', ["leet", "code"]))
        self.assertTrue(solution.wordBreak('applepenapple', ["apple", "pen"]))
        self.assertFalse(solution.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]))
        self.assertFalse(solution.wordBreak('a', []))
        self.assertTrue(solution.wordBreak('bb',
                                           ["a", "b", "bbb", "bbbb"]))


if __name__ == '__main__':
    unittest.main()
