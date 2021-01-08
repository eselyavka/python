#!/usr/bin/env python

import unittest


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        ss = []
        ts = []

        def process_string(s, stack):
            for c in s:
                if c == '#':
                    try:
                        stack.pop()
                    except IndexError:
                        pass
                    continue
                stack.append(c)

        process_string(S, ss)
        process_string(T, ts)

        return ss == ts


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
