#!/usr/bin/env python3

"""LeetCode solution 00243."""

import unittest

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        d = {}

        for i, word in enumerate(words):
            if word in d:
                d[word].append(i)
            else:
                d[word] = [i]

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
