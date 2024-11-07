#!/usr/bin/env python

import unittest

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        A_s = sum(A)
        B_s = sum(B)
        target = (A_s + B_s)//2

        setB = set(B)

        for num in A:
            if target - (A_s - num) in setB:
                return [num, target - (A_s - num)]

        return None

class TestSolution(unittest.TestCase):

    def test_fairCandySwap(self):
        solution = Solution()

        self.assertEqual(solution.fairCandySwap([1, 1], [2, 2]), [1, 2])
        self.assertEqual(solution.fairCandySwap([2], [1, 3]), [2, 3])
        self.assertEqual(solution.fairCandySwap([1, 2, 5], [2, 4]), [5, 4])

if __name__ == '__main__':
    unittest.main()
