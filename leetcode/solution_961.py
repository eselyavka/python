#!/usr/bin/env python

import unittest
from collections import defaultdict


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = defaultdict(int)

        for num in A:
            d[num] += 1

            if d.get(num, 0) > 1:
                return num


class TestSolution(unittest.TestCase):
    def test_repeatedNTimes(self):
        solution = Solution()
        self.assertEqual(solution.repeatedNTimes([1, 2, 3, 3]), 3)
        self.assertEqual(solution.repeatedNTimes([2, 1, 2, 5, 3, 2]), 2)
        self.assertEqual(solution.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]), 5)


if __name__ == '__main__':
    unittest.main()
