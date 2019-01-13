#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hash_A_B = defaultdict(int)
        for a in A:
            for b in B:
                hash_A_B[a+b] += 1

        res = 0

        for c in C:
            for d in D:
                _sum = c + d
                if _sum < 0:
                    if abs(_sum) in hash_A_B:
                        res += hash_A_B[abs(_sum)]
                else:
                    if -_sum in hash_A_B:
                        res += hash_A_B[-_sum]

        return res


class TestSolution(unittest.TestCase):
    def test_fourSumCount(self):
        solution = Solution()
        self.assertEqual(solution.fourSumCount([1, 2],
                                               [-2, -1],
                                               [-1, 2],
                                               [0, 2]), 2)

        self.assertEqual(solution.fourSumCount([-1, -1],
                                               [-1, 1],
                                               [-1, 1],
                                               [1, -1]), 6)

        self.assertEqual(solution.fourSumCount(
            [0, 1, -1],
            [-1, 1, 0],
            [0, 0, 1],
            [-1, 1, 1]), 17)


if __name__ == '__main__':
    unittest.main()
