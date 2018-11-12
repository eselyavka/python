#!/usr/bin/env python

import unittest

class Solution(object):
    def check_left(self, i, seats):
        if i > 0:
            d = 0
            while i > -1:
                if seats[i] == 1:
                    return d
                d += 1
                i -= 1

    def check_right(self, i, seats):
        if i < len(seats) - 1:
            d = 0
            while i < len(seats):
                if seats[i] == 1:
                    return d
                d += 1
                i += 1

    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        if not seats:
            return 0

        if len(seats) == 1:
            return 0

        if len(seats) == 2:
            return 1

        d = 0
        for i, seat in enumerate(seats):
            if seat:
                continue

            left_d = self.check_left(i, seats)
            right_d = self.check_right(i, seats)
            d = max(d, min(left_d if left_d else float('+inf'),
                           right_d if right_d else float('+inf')))

        return d

class TestSolution(unittest.TestCase):
    def test_maxDistToClosest(self):
        solution = Solution()
        self.assertEqual(solution.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]), 2)
        self.assertEqual(solution.maxDistToClosest([1, 0, 0, 0]), 3)
        self.assertEqual(solution.maxDistToClosest([0, 0, 0, 1]), 3)
        self.assertEqual(solution.maxDistToClosest([]), 0)
        self.assertEqual(solution.maxDistToClosest([1]), 0)
        self.assertEqual(solution.maxDistToClosest([1, 0]), 1)


if __name__ == '__main__':
    unittest.main()
