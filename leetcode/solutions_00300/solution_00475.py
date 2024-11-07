#!/usr/bin/env python

import unittest
import bisect

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        res = 0
        heaters.sort()
        for house in houses:
            less = bisect.bisect_right(heaters, house)
            distance_left = house - heaters[less - 1] if less > 0 else float('+inf')

            greater = bisect.bisect_left(heaters, house)
            distance_right = heaters[greater] - house if greater < len(heaters) else float('+inf')

            res = max(res, min(distance_left, distance_right))

        return res

class TestSolution(unittest.TestCase):
    def test_findRadius(self):
        solution = Solution()
        self.assertEqual(solution.findRadius([1, 5], [2]), 3)
        self.assertEqual(solution.findRadius([1, 2], [2]), 1)
        self.assertEqual(solution.findRadius([1, 2, 3], [2]), 1)
        self.assertEqual(solution.findRadius([1, 2, 3, 4], [1, 4]), 1)
        self.assertEqual(solution.findRadius([1, 2, 3, 4, 5, 6, 7, 8], [2, 7]), 2)
        self.assertEqual(solution.findRadius([1, 2, 3, 4], [1]), 3)
        self.assertEqual(solution.findRadius([1, 2, 3, 4], [4]), 3)
        self.assertEqual(solution.findRadius([1, 2, 3, 4], [2]), 2)
        self.assertEqual(solution.findRadius([1], [1, 2, 3, 4]), 0)


if __name__ == '__main__':
    unittest.main()
