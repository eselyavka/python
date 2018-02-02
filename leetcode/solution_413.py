#!/usr/bin/env python

import unittest

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        summ, tmp = 0, 0

        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                tmp += 1
                summ += tmp
            else:
                tmp = 0
        return

class TestSolution(unittest.TestCase):

    def test_numberOfArithmeticSlices(self):
        A = [1, 2, 3, 4]
        A2 = [1, 3, 5, 7, 9]
        A3 = [1, 1, 2, 5, 7]
        A4 = [1]
        A5 = [1, 2, 3]
        A6 = [1, 2, 3, 4, 5, 6]
        A7 = [1, 2, 3, 8, 9, 10]
        solution = Solution()
        self.assertEqual(solution.numberOfArithmeticSlices(A), 3)
        self.assertEqual(solution.numberOfArithmeticSlices(A2), 6)
        self.assertEqual(solution.numberOfArithmeticSlices(A3), 0)
        self.assertEqual(solution.numberOfArithmeticSlices(A4), 0)
        self.assertEqual(solution.numberOfArithmeticSlices(A5), 1)
        self.assertEqual(solution.numberOfArithmeticSlices(A6), 10)
        self.assertEqual(solution.numberOfArithmeticSlices(A7), 2)

if __name__ == '__main__':
    unittest.main()
