#!/usr/bin/env python3

"""LeetCode solution 01678."""

import unittest


class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res = ''
        for idx, char in enumerate(command):
            if char == 'G':
                res += 'G'
            elif char == ')':
                res += 'o' if command[idx - 1] == '(' else 'al'

        return res


class TestSolution(unittest.TestCase):
    def test_interpret(self):
        solution = Solution()
        self.assertEqual(solution.interpret('G()(al)'), 'Goal')
        self.assertEqual(solution.interpret('G()()()()(al)'), 'Gooooal')


if __name__ == '__main__':
    unittest.main()
