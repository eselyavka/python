#!/usr/bin/env python

import unittest

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stackS = []
        stackT = []

        for c in S:
            if c == '#':
                try:
                    stackS.pop()
                except IndexError:
                    pass
            else:
                stackS.append(c)

        for c in T:
            if c == '#':
                try:
                    stackT.pop()
                except IndexError:
                    pass
            else:
                stackT.append(c)

        return ''.join(stackS) == ''.join(stackT)

class TestSolution(unittest.TestCase):
    def test_backspaceCompare(self):
        solution = Solution()
        self.assertTrue(solution.backspaceCompare("ab#c", "ad#c"))
        self.assertTrue(solution.backspaceCompare("ab##", "c#d#"))
        self.assertTrue(solution.backspaceCompare("a##c", "#a#c"))
        self.assertFalse(solution.backspaceCompare("a#c", "b"))
        self.assertTrue(solution.backspaceCompare("y#fo##f", "y#f#o##f"))

if __name__ == '__main__':
    unittest.main()
