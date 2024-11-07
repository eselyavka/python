#!/usr/bin/env python

import unittest


class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 1:
            return 0

        x1, y1 = points[0]
        res = 0
        for i in range(1, len(points)):
            x2, y2 = points[i]
            res += max(abs(x2-x1), abs(y2-y1))
            x1, y1 = x2, y2

        return res


class TestSolution(unittest.TestCase):
    def test_minTimeToVisitAllPoints(self):
        solution = Solution()
        self.assertEqual(solution.minTimeToVisitAllPoints([[1, 1],
                                                           [3, 4],
                                                           [-1, 0]]), 7)


if __name__ == '__main__':
    unittest.main()
