#!/usr/bin/env python

import unittest
from collections import defaultdict
from copy import copy

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """

        alpha = defaultdict(int)

        for c in licensePlate:
            _lower = c.lower()
            if _lower.isalpha():
                alpha[_lower] += 1

        _min = [float('+inf'), None]

        for word in words:
            buf = copy(alpha)
            for c in word:
                if c in buf:
                    if buf[c]:
                        buf[c] -= 1

            if sum(buf.values()) == 0:
                if _min[0] > len(word):
                    _min[0] = len(word)
                    _min[1] = word

        return _min[1]

class TestSolution(unittest.TestCase):

    def test_shortestCompletingWord(self):
        solution = Solution()

        self.assertEqual(solution.shortestCompletingWord("1s3 PSt",
                                                         ["step",
                                                          "steps",
                                                          "stripe",
                                                          "stepple"]), "steps")
        self.assertEqual(solution.shortestCompletingWord("1s3 456",
                                                         ["looks",
                                                          "pest",
                                                          "stew",
                                                          "show"]), "pest")
        self.assertEqual(solution.shortestCompletingWord("GrC8950",
                                                         ["measure", "other",
                                                          "every", "base",
                                                          "according", "level",
                                                          "meeting", "none",
                                                          "marriage", "rest"]), "according")

if __name__ == '__main__':
    unittest.main()
