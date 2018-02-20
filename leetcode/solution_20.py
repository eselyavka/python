#!/usr/bin/env python

import unittest

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {'{':'}',
                    '(':')',
                    '[':']'}
        closing = brackets.values()
        stack = []
        c = ''

        for char in s:
            if char in brackets:
                stack.append(brackets[char])

            if char in closing:
                try:
                    c = stack.pop()
                except IndexError:
                    return False

                if char != c:
                    return False

        return not stack

class TestSolution(unittest.TestCase):

    def test_isValid(self):
        solution = Solution()
        valid = ['()', '()[]{}']
        invalid = ['(]', '([)]']
        invalid2 = ['(', ']']
        invalid3 = ['(((', ']]]']
        invalid4 = ['(((]', '(]]]']

        self.assertTrue(all([solution.isValid(s) for s in valid]))
        self.assertFalse(any([solution.isValid(s) for s in invalid]))
        self.assertFalse(any([solution.isValid(s) for s in invalid2]))
        self.assertFalse(any([solution.isValid(s) for s in invalid3]))
        self.assertFalse(any([solution.isValid(s) for s in invalid4]))

if __name__ == '__main__':
    unittest.main()
