#!/usr/bin/env python

import unittest

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        clean_string = s.strip()

        if not clean_string:
            return 0

        return len(clean_string.split()[-1])

class TestSolution(unittest.TestCase):
    def test_lengthOfLastWord(self):
        solution = Solution()
        self.assertEquals(solution.lengthOfLastWord('Hello World'), 5)

if __name__ == '__main__':
    unittest.main()
