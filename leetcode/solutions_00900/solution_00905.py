#!/usr/bin/env python

import unittest

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(A) - 1

        while left < right:
            if A[left] % 2 == 0 and A[right] % 2 == 0:
                left += 1
            elif A[left] % 2 == 1 and A[right] % 2 == 0:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
            elif A[left] % 2 == 0 and A[right] % 2 == 1:
                left += 1
                right -= 1
            else:
                right -= 1

        return A

class TestSolution(unittest.TestCase):

    def test_ArrayByParity(self):
        solution = Solution()

        self.assertListEqual(solution.sortArrayByParity([3, 1, 2, 4]), [4, 2, 1, 3])

if __name__ == '__main__':
    unittest.main()
