#!/usr/bin/env python

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

        arr = list()
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
