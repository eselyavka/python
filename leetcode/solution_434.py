#!/usr/bin/env python

import unittest
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

class TestSolution(unittest.TestCase):
    def test_countSegments(self):
        solution = Solution()
        self.assertEqual(solution.countSegments('Hello, my name is John'), 5)

if __name__ == '__main__':
    unittest.main()
