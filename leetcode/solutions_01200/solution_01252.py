#!/usr/bin/env python

import unittest
from collections import Counter


class Solution(object):
    def __init__(self):
        self.odd_number = 0

    def is_odd(self, number):
        return number % 2 == 1

    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        rows_cnt = Counter([t[0] for t in indices])
        col_cnt = Counter([t[1] for t in indices])

        for i in range(n):
            element = rows_cnt.get(i, 0)
            for j in range(m):
                element += col_cnt.get(j, 0)
                if self.is_odd(element):
                    self.odd_number += 1
                element -= col_cnt.get(j, 0)

        return self.odd_number


class TestSolution(unittest.TestCase):
    def test_oddCells(self):
        solution = Solution()
        self.assertEqual(solution.oddCells(2, 2, [[1, 1], [0, 0]]), 0)
        self.assertEqual(solution.oddCells(2, 3, [[0, 1], [1, 1]]), 6)


if __name__ == '__main__':
    unittest.main()
