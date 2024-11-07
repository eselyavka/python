#!/usr/bin/env python

import unittest

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True

        _dir_in = False
        _dir_dec = False
        for i in range(1, len(A) - 1):
            if A[i-1] <= A[i] <= A[i+1] and not _dir_in:
                _dir_in = False if A[i] == A[i-1] == A[i+1] else True
            if A[i-1] >= A[i] >= A[i+1] and not _dir_dec:
                _dir_dec = False if A[i] == A[i-1] == A[i+1] else True

            if not (A[i-1] <= A[i] <= A[i+1] or A[i-1] >= A[i] >= A[i+1]):
                return False

        return False if all([_dir_in, _dir_dec]) else True

class TestSolution(unittest.TestCase):

    def test_isMonotonic(self):

        solution = Solution()

        self.assertTrue(solution.isMonotonic([1, 2, 2, 3]))
        self.assertTrue(solution.isMonotonic([6, 5, 4, 4]))
        self.assertFalse(solution.isMonotonic([1, 3, 2]))
        self.assertTrue(solution.isMonotonic([1, 2, 4, 5]))
        self.assertTrue(solution.isMonotonic([1, 1, 1]))
        self.assertTrue(solution.isMonotonic([1]))
        self.assertTrue(solution.isMonotonic([1, 2]))
        self.assertTrue(solution.isMonotonic([2, 1]))
        self.assertFalse(solution.isMonotonic([11, 11, 9, 4, 3, 3, 3, 1, -1, -1, 3, 3, 3, 5, 5, 5]))
        self.assertFalse(solution.isMonotonic([997, 997, 998, 998, 998, 999, 999, 1000, 1000, 999]))

if __name__ == '__main__':
    unittest.main()
