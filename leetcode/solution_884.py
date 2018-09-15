#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        dA = defaultdict(int)
        dB = defaultdict(int)

        AS = A.split(" ")
        BS = B.split(" ")

        for word in AS:
            dA[word] += 1

        for word in BS:
            dB[word] += 1

        res = []
        for word in set(AS) ^ set(BS):
            if not ((word in dA and dA[word] > 1) or (word in dB and dB[word] > 1)):
                res.append(word)

        return res

class TestSolution(unittest.TestCase):

    def test_uncommonFromSentences(self):
        solution = Solution()

        self.assertListEqual(
            solution.uncommonFromSentences("this apple is sweet", "this apple is sour"),
            ["sweet", "sour"])
        self.assertListEqual(solution.uncommonFromSentences("apple apple", "banana"), ["banana"])

if __name__ == '__main__':
    unittest.main()
