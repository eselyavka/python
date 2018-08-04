#!/usr/bin/env python

import unittest

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """

        if len(intervals) == 1:
            return True

        intervals.sort(key=lambda x: x[1])
        size = len(intervals)

        for i in range(size - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False

        return True

class TestSolution(unittest.TestCase):
    def test_canAttendMeetings(self):
        solution = Solution()
        self.assertFalse(solution.canAttendMeetings([[0, 30],
                                                     [5, 10],
                                                     [15, 20]]))
        self.assertTrue(solution.canAttendMeetings([[7, 10],
                                                    [2, 4]]))

if __name__ == '__main__':
    unittest.main()
