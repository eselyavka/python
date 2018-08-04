#!/usr/bin/env python

import unittest

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        size = len(intervals)

        if size == 1:
            return 1

        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        s, e, rooms, available = 0, 0, 0, 0

        while s < size - 1:
            if start[s] < end[e]:
                if available == 0:
                    rooms += 1
                else:
                    available -= 1
                s += 1
            else:
                available += 1
                e += 1

        return rooms

class TestSolution(unittest.TestCase):
    def test_minMeetingRooms(self):
        solution = Solution()
        self.assertEqual(solution.minMeetingRooms([[0, 30],
                                                   [5, 10],
                                                   [15, 20]]), 2)
        self.assertEqual(solution.minMeetingRooms([[7, 10],
                                                   [2, 4]]), 1)
        self.assertEqual(solution.minMeetingRooms([]), 0)
        self.assertEqual(solution.minMeetingRooms([[2, 11],
                                                   [6, 16],
                                                   [11, 16]]), 2)

if __name__ == '__main__':
    unittest.main()
