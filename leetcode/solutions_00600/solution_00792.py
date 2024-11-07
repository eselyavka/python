#!/usr/bin/env python

import unittest
from collections import defaultdict
import bisect

class Solution(object):
    def isSubsequence(self, word, d):
        j = 0
        for c in word:
            if c not in d or d[c][-1] < j:
                return False
            j = d[c][bisect.bisect_left(d[c], j)] + 1

        return True


    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        d = defaultdict(list)

        for i, c in enumerate(S):
            d[c].append(i)

        return sum([self.isSubsequence(word, d) for word in words])


class TestSolution(unittest.TestCase):
    def test_numMatchingSubseq(self):
        solution = Solution()
        self.assertEqual(solution.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]), 3)
        self.assertEqual(solution.numMatchingSubseq("dsahjpjauf",
                                                    ["ahjpjau",
                                                     "ja",
                                                     "ahbwzgqnuk",
                                                     "tnmlanowax"]), 2)

if __name__ == '__main__':
    unittest.main()
