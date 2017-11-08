#!/usr/bin/env python

import unittest

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        d = dict()

        for i in range(len(words)):
            if d.has_key(words[i]):
                d[words[i]].append(i)
            else:
                d[words[i]] = [i]

        if len(d[word1]) < len(d[word2]):
            d[word1] + [0 for _ in range(len(d[word2]) - len(d[word1]))]
        elif len(d[word1]) > len(d[word2]):
            d[word2] + [0 for _ in range(len(d[word1]) - len(d[word2]))]

        res = []
        for pos1 in d[word1]:
            for pos2 in d[word2]:
                res.append(abs(pos1 - pos2))

        return min(res)

class TestSolution(unittest.TestCase):

    def test_shortestDistance(self):
        arr = ["practice", "makes", "perfect", "coding", "makes"]
        arr2 = ["a", "a", "b", "b"]
        solution = Solution()
        self.assertEqual(solution.shortestDistance(arr, "coding", "practice"), 3)
        self.assertEqual(solution.shortestDistance(arr, "coding", "makes"), 1)
        self.assertEqual(solution.shortestDistance(arr2, "a", "b"), 1)

if __name__ == '__main__':
    unittest.main()
