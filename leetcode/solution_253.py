#!/usr/bin/env python

import unittest


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        start_points = sorted([t[0] for t in intervals])
        end_points = sorted([t[1] for t in intervals])

        n = len(intervals)
        s, e, ans, count = [0] * 4

        while s < n:
            if start_points[s] < end_points[e]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
            ans = max(ans, count)

        return ans

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
