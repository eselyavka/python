#!/usr/bin/env python

import unittest


class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if len(words[i]) > len(words[j]):
                    continue
                if words[i] in words[j]:
                    s.add(words[i])

        return list(s)


class TestSolution(unittest.TestCase):

    def test_stringMatching(self):
        solution = Solution()
        self.assertEqual(solution.stringMatching(
            ["leetcoder", "leetcode", "od", "hamlet", "am"]),
                         ["leetcode", "od", "am"])


if __name__ == '__main__':
    unittest.main()
