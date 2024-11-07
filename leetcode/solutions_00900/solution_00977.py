#!/usr/bin/env python

import unittest

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return A

        left, right, i = 0, len(A) - 1, len(A) - 1
        res = [None] * len(A)

        while left <= right:
            if abs(A[right]) > abs(A[left]):
                res[i] = A[right]**2
                right -= 1
            else:
                res[i] = A[left]**2
                left += 1
            i -= 1

        return res


class TestSolution(unittest.TestCase):
    def test_sortedSquares(self):
        solution = Solution()
        self.assertListEqual(solution.sortedSquares([]), [])
        self.assertEqual(solution.sortedSquares(None), None)
        self.assertListEqual(solution.sortedSquares([0]), [0])
        self.assertListEqual(solution.sortedSquares([-1]), [1])
        self.assertListEqual(solution.sortedSquares([10]), [100])
        self.assertListEqual(solution.sortedSquares([-3, -3, -2, 1]), [1, 4, 9, 9])
        self.assertListEqual(solution.sortedSquares([-1, 0, 1, 1]), [0, 1, 1, 1])
        self.assertListEqual(solution.sortedSquares([-5, 10]), [25, 100])
        self.assertListEqual(solution.sortedSquares([4, 10]), [16, 100])
        self.assertListEqual(solution.sortedSquares([-3, 0, 3]), [0, 9, 9])
        self.assertListEqual(solution.sortedSquares([3, 3, 3]), [9, 9, 9])
        self.assertListEqual(solution.sortedSquares([-1, 0, 1, 1]), [0, 1, 1, 1])
        self.assertListEqual(solution.sortedSquares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        self.assertListEqual(solution.sortedSquares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])


if __name__ == '__main__':
    unittest.main()
