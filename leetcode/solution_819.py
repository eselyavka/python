#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def _replace(self, paragraph, punct):
        if not punct:
            return paragraph.split()

        return self._replace(' '.join(paragraph.split(punct[0])), punct[1:])

    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        if not paragraph:
            return ''

        d = defaultdict(int)
        punct = ["!", "?", "'", ",", ";", "."]

        for word in self._replace(paragraph, punct):
            d[word.lower()] += 1

        res = d.items()
        res.sort(key=lambda t: t[1], reverse=True)

        for item in res:
            if item[0] not in banned:
                return item[0]

        return ''

class TestSolution(unittest.TestCase):
    def test_mostCommonWord(self):
        solution = Solution()
        self.assertEqual(solution.mostCommonWord("Bob hit a ball, the hit BALL \
                                                  flew far after it was hit.",
                                                 ["hit"]),
                         "ball")
        self.assertEqual(solution.mostCommonWord("a, a, a, a, b,b,b,c, c", "a"), "b")

if __name__ == '__main__':
    unittest.main()
