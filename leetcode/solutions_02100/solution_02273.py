#!/usr/bin/env python

import unittest
from collections import defaultdict


class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        acc = defaultdict(list)

        for i, word in enumerate(words):
            key = ''.join(sorted(word))
            prev = acc.get(key)
            if prev:
                t = (i, not i - prev[-1][0] == 1)
                acc[key].append(t)
            else:
                t = (i, True)
                acc[key].append(t)

        res = [None for _ in range(len(words))]

        for key in acc:
            for idx_stat in acc[key]:
                idx, pick = idx_stat
                if pick:
                    res[idx] = words[idx]

        return [w for w in res if w is not None]


class TestSolution(unittest.TestCase):
    def test_removeAnagrams(self):
        solution = Solution()
        self.assertListEqual(solution.removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"]), ["abba", "cd"])


if __name__ == '__main__':
    unittest.main()
