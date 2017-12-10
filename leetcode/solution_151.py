#!/usr/bin/env python

import unittest

class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return ' '.join(s.split()[::-1])

class TestSolution(unittest.TestCase):

    def test_reverseWords(self):
        s = "the sky is blue"

        solution = Solution()
        self.assertEqual(solution.reverseWords(s), "blue is sky the")

if __name__ == '__main__':
    unittest.main()
