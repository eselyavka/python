#!/usr/bin/env python

import unittest
from collections import defaultdict


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        res = 0

        for p_1 in points:
            x_1, y_1 = p_1
            distances = defaultdict(int)
            for p_2 in points:
                x_2, y_2 = p_2
                distance = ((x_2-x_1)**2 + (y_2 - y_1)**2) ** 0.5
                distances[distance] += 1

            for key in distances:
                res += distances[key] * (distances[key] - 1)

        return res


class TestSolution(unittest.TestCase):
    def test_numberOfBoomerangs(self):
        solution = Solution()
        self.assertEqual(solution.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]), 2)


if __name__ == '__main__':
    unittest.main()
