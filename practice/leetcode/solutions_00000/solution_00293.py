#!/usr/bin/env python3

"""LeetCode solution 00293."""

import unittest

class Solution(object):
    def _nextMove(self, s, arr, idx=0):

        if idx > len(s):
            return

        if s[idx:idx+2] == '++':
            arr.append(''.join(s[:idx] + '--' + s[idx+2:]))

        self._nextMove(s, arr, idx=idx+1)

    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        arr = []
        self._nextMove(s, arr)
        return arr

class TestSolution(unittest.TestCase):

    def test_generatePossibleNextMoves(self):
        s = "++++"
        solution = Solution()
        self.assertEqual(solution.generatePossibleNextMoves(s),
                         ["--++",
                          "+--+",
                          "++--"
                         ])

if __name__ == '__main__':
    unittest.main()
