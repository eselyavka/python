#!/usr/bin/python

import unittest

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """


        if not digits:
            return []

        mapping = {'2':'abc',
                   '3':'def',
                   '4':'ghi',
                   '5':'jkl',
                   '6':'mno',
                   '7':'pqrs',
                   '8':'tuv',
                   '9':'wxyz'}

        acc = []

        def _rec(prefix, idx=0):
            if idx < len(digits):
                for char in mapping[digits[idx]]:
                    _rec(prefix + char, idx+1)
            else:
                acc.append(prefix)

        _rec("")

        return acc

class TestSolution(unittest.TestCase):

    def test_letterCombinations(self):
        solution = Solution()

        self.assertEqual(sorted(solution.letterCombinations('23')),
                         ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self.assertEqual(sorted(solution.letterCombinations('')), [])
        self.assertEqual(sorted(solution.letterCombinations('4')), ['g', 'h', 'i'])

if __name__ == '__main__':
    unittest.main()
