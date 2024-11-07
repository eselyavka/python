#!/usr/bin/env python

import unittest

class Solution(object):

    def _rec(self, n, mas=None):
        if n == 1:
            return mas

        arr = list()

        if mas is None:
            payload = range(1, n+1)
            for i in range(len(payload)/2):
                arr.append('(' + str(payload[i]) + ',' + str(payload[(len(payload) - 1) - i]) + ')')
        else:
            for i in range(len(mas)/2):
                arr.append('(' + mas[i] + ',' + str(mas[(len(mas) - 1) - i]) + ')')
        return arr + self._rec(n/2, arr)

    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """

        return self._rec(n).pop()

class TestSolution(unittest.TestCase):

    def test_findContestMatch(self):
        solution = Solution()
        self.assertEqual(solution.findContestMatch(2), '(1,2)')
        self.assertEqual(solution.findContestMatch(4), '((1,4),(2,3))')
        self.assertEqual(solution.findContestMatch(8), '(((1,8),(4,5)),((2,7),(3,6)))')

if __name__ == '__main__':
    unittest.main()
