#!/usr/bin/env python3

"""LeetCode solution 03163."""

import unittest


class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """

        i = 0
        comm = ""
        while i < len(word):
            j = i + 1
            cnt = 1
            while j < len(word) and word[i] == word[j]:
                cnt += 1
                if cnt == 9:
                    comm += f"{cnt}{word[i]}"
                    cnt = 0
                j += 1
            if cnt != 0:
                comm += f"{cnt}{word[i]}"
            i = j
        return comm


class TestSolution(unittest.TestCase):
    def test_compressedString(self):
        solution = Solution()
        self.assertEqual(solution.compressedString("abcde"), "1a1b1c1d1e")
        self.assertEqual(solution.compressedString("aaaaaaaaaaaaaabb"), "9a5a2b")
        self.assertEqual(solution.compressedString("aaaaaaaaay"), "9a1y")


if __name__ == '__main__':
    unittest.main()
