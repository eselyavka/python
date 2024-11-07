#!/usr/bin/env python

import unittest

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return (word == word.lower() or
                word == word.upper() or
                word == word[0].upper() +
                word[1:].lower()) if word else False

class TestSolution(unittest.TestCase):

    def test_detectCapitalUse(self):
        data = 'USA'
        data1 = 'FlaG'

        solution = Solution()
        self.assertTrue(solution.detectCapitalUse(data))
        self.assertFalse(solution.detectCapitalUse(data1))

if __name__ == '__main__':
    unittest.main()
