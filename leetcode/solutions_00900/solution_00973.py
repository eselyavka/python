#!/usr/bin/env python

import unittest
import math


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        res = []
        x1, y1 = 0, 0
        for point in points:
            x2, y2 = point
            distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            res.append((distance, point))

        res.sort(key=lambda t: t[0])

        return [x[1] for x in res[:K]]


class TestSolution(unittest.TestCase):

    def test_kClosest(self):
        solution = Solution()
        self.assertListEqual(solution.kClosest([[1, 3], [-2, 2]], 1),
                             [[-2, 2]])


if __name__ == '__main__':
    unittest.main()
