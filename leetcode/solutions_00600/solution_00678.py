#!/usr/bin/env python

import unittest


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        lo, hi = 0, 0

        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                if lo > 0:
                    lo -= 1
                hi -= 1
            else:
                if lo > 0:
                    lo -= 1
                hi += 1

            if hi < 0:
                return False

        return not lo


class TestSolution(unittest.TestCase):
    def test_checkValidString(self):
        solution = Solution()
        self.assertTrue(solution.checkValidString('(*))'))


if __name__ == '__main__':
    unittest.main()
