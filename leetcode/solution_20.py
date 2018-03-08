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

    def isValid2(self, s):
        def matches(open_par, close_par):
            _open = '({['
            closing = ')}]'
            return _open.index(open_par) == closing.index(close_par)

        balanced = True
        idx = 0
        stack = []

        while idx < len(s) and balanced:
            if s[idx] in '({[':
                stack.append(s[idx])
            else:
                if not stack:
                    balanced = False
                else:
                    r = stack.pop()
                    if not matches(r, s[idx]):
                        balanced = False
            idx += 1

        if not balanced or stack:
            return False

        return True

class TestSolution(unittest.TestCase):

    def test_isValid(self):
        solution = Solution()
        valid = ['()', '()[]{}']
        invalid = ['(]', '([)]']
        invalid2 = ['(', ']']
        invalid3 = ['(((', ']]]']
        invalid4 = ['(((]', '(]]]']
        valid2 = ['(asds234)[kk{lll}120]', '{pppp}']

        self.assertTrue(all([solution.isValid(s) for s in valid]))
        self.assertFalse(any([solution.isValid(s) for s in invalid]))
        self.assertFalse(any([solution.isValid(s) for s in invalid2]))
        self.assertFalse(any([solution.isValid(s) for s in invalid3]))
        self.assertFalse(any([solution.isValid(s) for s in invalid4]))
        self.assertTrue(all([solution.isValid(s) for s in valid2]))

    def test_isValid2(self):
        solution = Solution()
        valid = ['()', '[(){}]']
        invalid = ['(]', '([)]']
        invalid2 = ['(', ']']
        invalid3 = ['(((', ']]]']
        invalid4 = ['(((]', '(]]]']

        self.assertTrue(all([solution.isValid2(s) for s in valid]))
        self.assertFalse(any([solution.isValid2(s) for s in invalid]))
        self.assertFalse(any([solution.isValid2(s) for s in invalid2]))
        self.assertFalse(any([solution.isValid2(s) for s in invalid3]))
        self.assertFalse(any([solution.isValid2(s) for s in invalid4]))

if __name__ == '__main__':
    unittest.main()
