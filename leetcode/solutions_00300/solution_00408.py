#!/usr/bin/env python

import unittest

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if str(len(word)) == abbr:
            return True

        i, j = 0, 0
        m, n = len(word), len(abbr)

        while i < m and j < n:
            # case chars are equal
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue

            # if letters doesn't match
            if word[i] != abbr[j] and abbr[j].isalpha():
                return False

            # hit a digit
            if word[i] != abbr[j]:
                num = 0
                while j < n and abbr[j].isdigit():
                    if num == 0 and int(abbr[j]) == 0:
                        return False
                    num = num * 10 + int(abbr[j])
                    j += 1

                # advance i
                i += num

        return i == m and j == n

class TestSolution(unittest.TestCase):
    def test_validWordAbbreviation(self):
        solution = Solution()
        self.assertTrue(solution.validWordAbbreviation("internationalization", "i12iz4n"))

if __name__ == '__main__':
    unittest.main()
