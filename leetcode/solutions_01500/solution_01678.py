#!/usr/bin/env python

import unittest


class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res = ''
        for idx in range(len(command)):
            if command[idx] == 'G':
                res += 'G'
            elif command[idx] == ')':
                res += 'o' if command[idx - 1] == '(' else 'al'

        return res


class TestSolution(unittest.TestCase):
    def test_interpret(self):
        solution = Solution()
        self.assertEqual(solution.interpret('G()(al)'), 'Goal')
        self.assertEqual(solution.interpret('G()()()()(al)'), 'Goooal')


if __name__ == '__main__':
    unittest.main()
