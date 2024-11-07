#!/usr/bin/env python

import unittest

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        sn = {'0':'0', '1':'1', '8':'8', '9':'6', '6':'9'}

        res = ''
        for c in str(num):
            try:
                res += sn[c]
            except KeyError:
                pass

        return str(num) == res[::-1]

class TestSolution(unittest.TestCase):
    def test_isStrobogrammatic(self):
        solution = Solution()
        self.assertTrue(solution.isStrobogrammatic(88))
        self.assertTrue(solution.isStrobogrammatic(69))
        self.assertFalse(solution.isStrobogrammatic(34))
        self.assertFalse(solution.isStrobogrammatic(6))

if __name__ == '__main__':
    unittest.main()
