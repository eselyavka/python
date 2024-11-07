#!/usr/bin/env python

import unittest


class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        min_deg = minutes * 6.0
        hour_deg = hour * 30.0 + minutes * 0.5

        res = min(abs(hour_deg - min_deg), 360.0 - abs(hour_deg - min_deg))

        return res


class TestSolution(unittest.TestCase):

    def test_angleClock(self):
        solution = Solution()
        self.assertEqual(solution.angleClock(10, 12), 126.0)


if __name__ == '__main__':
    unittest.main()
