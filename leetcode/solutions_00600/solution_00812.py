#!/usr/bin/env python

import unittest


class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        if not points:
            return 0

        max_ = 0
        for i in range(len(points) - 2):
            for j in range(i+1, len(points) - 1):
                for l in range(j+1, len(points)):
                    p1, p2, p3 = points[i], points[j], points[l]
                    local_max = 0.5 * abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))
                    max_ = max(local_max, max_)

        return max_


class TestSolution(unittest.TestCase):

    def test_largestTriangleArea(self):
        solution = Solution()
        self.assertEqual(solution.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]), 2.0)
        self.assertEqual(solution.largestTriangleArea([[4, 6], [6, 5], [3, 1]]), 5.5)


if __name__ == '__main__':
    unittest.main()
