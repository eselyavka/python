#!/usr/bin/env python

import unittest

class Solution(object):
    def is_arithmetic_subsequence(self, A):
        for i in range(2, len(A)):
            if A[i] - A[i-1] != A[i-1] - A[i-2]:
                return False
        return True

    def _rec(self, A, i, j, slice_len):
        if slice_len > len(A):
            return 0

        if j <= len(A):
            arr = A[i:j]
            return ((1 if self.is_arithmetic_subsequence(arr) else 0) +
                    self._rec(A, i+1, j+1, slice_len))
        return self._rec(A, 0, slice_len+1, slice_len+1)

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return self._rec(A, 0, 3, 3)

class TestSolution(unittest.TestCase):

    def test_numberOfArithmeticSlices(self):
        A = [1, 2, 3, 4]
        A2 = [1, 3, 5, 7, 9]
        A3 = [1, 1, 2, 5, 7]
        A4 = [1]
        A5 = [1, 2, 3]
        A6 = [1, 2, 3, 4, 5, 6]
        A7 = [1, 2, 3, 8, 9, 10]
        A8 = [2, 4, 6, 8, 10]
        solution = Solution()
        self.assertEqual(solution.numberOfArithmeticSlices(A), 3)
        self.assertEqual(solution.numberOfArithmeticSlices(A2), 6)
        self.assertEqual(solution.numberOfArithmeticSlices(A3), 0)
        self.assertEqual(solution.numberOfArithmeticSlices(A4), 0)
        self.assertEqual(solution.numberOfArithmeticSlices(A5), 1)
        self.assertEqual(solution.numberOfArithmeticSlices(A6), 10)
        self.assertEqual(solution.numberOfArithmeticSlices(A7), 2)
        self.assertEqual(solution.numberOfArithmeticSlices(A8), 7)

if __name__ == '__main__':
    unittest.main()
