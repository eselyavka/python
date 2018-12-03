#!/usr/bin/env python

import unittest

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return False

        if len(A) < 3:
            return False

        _max = max(A)

        for i in range(1, len(A) - 1):
            if not (A[i-1] < A[i] < A[i+1] or
                    A[i-1] < A[i] > A[i+1] or
                    A[i-1] > A[i] > A[i+1]):
                return False

        return False if (A[0] == _max or A[-1] == _max) else True


class TestSolution(unittest.TestCase):
    def test_validMountainArray(self):
        solution = Solution()
        self.assertFalse(solution.validMountainArray([2, 1]))
        self.assertFalse(solution.validMountainArray([3, 5, 5]))
        self.assertTrue(solution.validMountainArray([0, 3, 2, 1]))
        self.assertFalse(solution.validMountainArray([0, 1, 2, 3]))
        self.assertFalse(solution.validMountainArray([3, 2, 1, 0]))
        self.assertTrue(solution.validMountainArray([0, 1, 2, 3, 5, 4, 3, 2, 1]))
        self.assertFalse(solution.validMountainArray([3, 7, 6, 4, 3, 0, 1, 0]))


if __name__ == '__main__':
    unittest.main()
