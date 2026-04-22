#!/usr/bin/env python3

"""LeetCode solution 02452."""

import unittest


class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """

        def within_two(word, target):
            edits = 0
            for a, b in zip(word, target):
                if a != b:
                    edits += 1
                    if edits > 2:
                        return False

            return True

        ans = []
        for query in queries:
            for word in dictionary:
                if within_two(query, word):
                    ans.append(query)
                    break

        return ans


class TestSolution(unittest.TestCase):
    def test_twoEditWords(self):
        solution = Solution()
        self.assertListEqual(solution.twoEditWords(["word", "note", "ants", "wood"],
                                                   ["wood", "joke", "moat"]),
                             ["word", "note", "wood"])


if __name__ == '__main__':
    unittest.main()
