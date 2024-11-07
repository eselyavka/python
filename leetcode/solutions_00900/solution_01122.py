#!/usr/bin/env python

import unittest
from collections import Counter


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        c = Counter(arr1)
        res = []
        for num in arr2:
            res.extend([num] * c.get(num))
            c[num] = 0
        rest = []
        for num in c:
            if c[num] > 0:
                rest.extend([num] * c[num])
        rest.sort()
        res.extend(rest)

        return res


class TestSolution(unittest.TestCase):
    def test_relativeSortArray(self):
        solution = Solution()
        self.assertEqual(solution.relativeSortArray(
            [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
            [2, 1, 4, 3, 9, 6]), [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19])
        self.assertEqual(solution.relativeSortArray(
            [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31],
            [2, 42, 38, 0, 43, 21]),
                         [2, 42, 38, 0, 43, 21, 5, 7, 12, 12, 13, 23,
                          24, 24, 27, 29, 30, 31, 33, 48])


if __name__ == '__main__':
    unittest.main()
