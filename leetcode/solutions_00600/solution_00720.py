#!/usr/bin/env python

import unittest

class Solution(object):

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        words.sort()
        res = ''
        s = set()

        for word in words:
            if len(word) == 1 or word[:-1] in s:
                s.add(word)
                res = word if len(res) < len(word) else res
        return res

class TestSolution(unittest.TestCase):

    def test_longestWord(self):
        words = ["w", "wo", "wor", "worl", "world"]
        words2 = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        words3 = ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm",
                  "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]
        words4 = ["m", "mo", "moc", "moch", "mocha", "l", "la",
                  "lat", "latt", "latte", "c", "ca", "cat"]

        solution = Solution()
        self.assertEqual(solution.longestWord(words), "world")
        self.assertEqual(solution.longestWord(words2), "apple")
        self.assertEqual(solution.longestWord(words3), "yodn")
        self.assertEqual(solution.longestWord(words4), "latte")

if __name__ == '__main__':
    unittest.main()
