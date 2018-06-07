#!/usr/bin/env python

import unittest

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split(' ')):
            return False

        return (len(set(zip(pattern, str.split(' ')))) ==
                len(set(pattern)) ==
                len(set(str.split(' '))))

class TestSolution(unittest.TestCase):

    def test_wordPattern(self):
        solution = Solution()

        self.assertTrue(solution.wordPattern("abba", "dog cat cat dog"))
        self.assertFalse(solution.wordPattern("abba", "dog cat cat fish"))
        self.assertFalse(solution.wordPattern("aaaa", "dog cat cat dog"))
        self.assertFalse(solution.wordPattern("abba", "dog dog dog dog"))
        self.assertFalse(solution.wordPattern("aba", "cat cat cat dog"))
        self.assertTrue(solution.wordPattern("abc", "b c a"))
        self.assertTrue(solution.wordPattern("tqbfjotld",
                                             "the quick brown fox jumps over the lazy dog"))
        self.assertFalse(solution.wordPattern("jquery", "jquery"))

if __name__ == '__main__':
    unittest.main()
