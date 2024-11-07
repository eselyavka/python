#!/usr/bin/env python

import unittest

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for word in words:
            if len(set(word)) != len(set(pattern)):
                continue

            mapping = dict(zip(pattern, word))

            actual = ''
            for c in pattern:
                actual += mapping[c]

            if word == actual:
                res.append(word)

        return res


class TestSolution(unittest.TestCase):

    def test_findAndReplacePattern(self):
        solution = Solution()

        self.assertListEqual(solution.findAndReplacePattern(
            ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"),
                             ["mee", "aqq"])
        self.assertListEqual(solution.findAndReplacePattern(
            ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "xyz"),
                             ["abc", "deq"])
        self.assertListEqual(solution.findAndReplacePattern(
            ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "kkk"),
                             ["ccc"])
        self.assertListEqual(solution.findAndReplacePattern(["abc"], "xyz"), ["abc"])
        self.assertListEqual(solution.findAndReplacePattern(["abc"], "xxz"), [])


if __name__ == '__main__':
    unittest.main()
