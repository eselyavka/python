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
        ab_dict = defaultdict(int)

        for a in A:
            for b in B:
                ab_dict[a + b] += 1

        res = 0
        for c in C:
            for d in D:
                sum_ = c + d
                res += ab_dict.get(abs(sum_) if sum_ < 0 else -sum_, 0)

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
