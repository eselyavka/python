#!/usr/bin/env python

import unittest

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = dict(zip(order, range(len(order))))

        def alien_cmp(word1, word2):
            i = 0
            while i < min(len(word1), len(word2)):
                if d[word1[i]] == d[word2[i]]:
                    i += 1
                elif d[word1[i]] < d[word2[i]]:
                    return -1
                else:
                    return 1

            if len(word1) == len(word2):
                return 0
            elif len(word1) > len(word2):
                return 1

            return -1

        original = words[:]
        words.sort(cmp=alien_cmp)

        return words == original

class TestSolution(unittest.TestCase):
    def test_isAlienSorted(self):
        solution = Solution()
        self.assertTrue(solution.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
        self.assertTrue(solution.isAlienSorted(["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz"))
        self.assertFalse(solution.isAlienSorted(["word", "world", "row"],
                                                "worldabcefghijkmnpqstuvxyz"))
        self.assertFalse(solution.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
        self.assertTrue(solution.isAlienSorted(["ubg", "kwh"], "qcipyamwvdjtesbghlorufnkzx"))


if __name__ == '__main__':
    unittest.main()
