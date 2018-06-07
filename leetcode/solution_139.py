#!/usr/bin/env python

import unittest

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict and not s:
            return True

        if not wordDict and s:
            return False

        if not s and wordDict:
            return False

        def in_dict(s):
            return s in wordDict

        size = len(s)
        wb = [False] * (size+1)
        for i in range(1, size+1):
            if not wb[i] and in_dict(s[:i]):
                wb[i] = True
            if wb[i]:
                if i == size:
                    return True
                for j in range(i, size+1):
                    if not wb[j] and in_dict(s[i:j]):
                        wb[j] = True
                    if j == size and wb[j]:
                        return True

        return False

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
