#!/usr/bin/env python

import unittest


class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        cw, ccw = 0, 0
        i = start
        while i != destination:
            cw += distance[i]
            if i == len(distance) - 1:
                i = 0
            else:
                i += 1

        i = start
        while i != destination:
            if i == 0:
                i = len(distance) - 1
            else:
                i -= 1
            ccw += distance[i]

        return min(cw, ccw)


class TestSolution(unittest.TestCase):
    def test_distanceBetweenBusStops(self):
        solution = Solution()
        self.assertEqual(solution.distanceBetweenBusStops([1, 2, 3, 4], 0, 1), 1)


if __name__ == '__main__':
    unittest.main()
