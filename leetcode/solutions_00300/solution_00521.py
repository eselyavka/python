#!/usr/bin/env python

import unittest

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """

        if a == b:
            return -1

        return max(len(a), len(b))

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.words = "aba", "cdc"
        self.words2 = "aaa", "aaa"
        self.words3 = "aefawfawfawfaw", "aefawfeawfwafwaef"

    def test_findLUSlength(self):
        solution = Solution()
        self.assertEqual(solution.findLUSlength(*self.words), 3)
        self.assertEqual(solution.findLUSlength(*self.words2), -1)
        self.assertEqual(solution.findLUSlength(*self.words3), 17)

if __name__ == '__main__':
    unittest.main()
