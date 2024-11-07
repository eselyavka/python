#!/usr/bin/env python

import unittest


class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        spaces = text.count(' ')

        if not spaces:
            return text

        words = text.split()

        if len(words) == 1:
            return words[0] + ' ' * spaces

        num = spaces // ((len(words) - 1) or 1)
        rest = spaces % ((len(words) - 1) or 1)

        res = ''
        for i, word in enumerate(words):
            res += word
            res += ' ' * num if i < len(words) - 1 else ''

        return res + ' ' * rest


class TestSolution(unittest.TestCase):
    def test_reorderSpaces(self):
        solution = Solution()
        self.assertEqual(solution.reorderSpaces("  this   is  a sentence "),
                         "this   is   a   sentence")


if __name__ == '__main__':
    unittest.main()
