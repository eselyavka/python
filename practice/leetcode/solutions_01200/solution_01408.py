#!/usr/bin/env python3

"""LeetCode solution 01408."""

import unittest


class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for i, word in enumerate(words):
            for j, other_word in enumerate(words):
                if i == j:
                    continue
                if len(word) > len(other_word):
                    continue
                if word in other_word:
                    res.append(word)
                    break

        return res


class TestSolution(unittest.TestCase):

    def test_stringMatching(self):
        solution = Solution()
        self.assertEqual(solution.stringMatching(
            ["leetcoder", "leetcode", "od", "hamlet", "am"]),
                         ["leetcode", "od", "am"])


if __name__ == '__main__':
    unittest.main()
