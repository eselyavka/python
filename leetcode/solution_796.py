#!/usr/bin/env python

import unittest

class Solution(object):
    def _rec(self, A, B, i):
        if A == B:
            return True
        if i >= len(A):
            return False

        return self._rec(A[1:]+A[0], B, i+1)

    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        return self._rec(A, B, 0)

class TestSolution(unittest.TestCase):

    def test_rotateString(self):
        A = 'abcde'
        B = 'cdeab'
        A1 = 'abcde'
        B1 = 'abced'
        A2 = ''
        B2 = ''
        solution = Solution()
        self.assertTrue(solution.rotateString(A, B))
        self.assertFalse(solution.rotateString(A1, B1))
        self.assertTrue(solution.rotateString(A2, B2))

if __name__ == '__main__':
    unittest.main()
