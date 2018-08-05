#!/usr/bin/env python

import unittest

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        stack = [intervals[0]]
        i = 1

        while i < len(intervals):
            interval = stack.pop()
            if interval[1] >= intervals[i][0]:
                if intervals[i][1] > interval[1]:
                    interval[1] = intervals[i][1]
                    stack.append(interval)
                else:
                    stack.append(interval)
            else:
                stack.append(interval)
                stack.append(intervals[i])
            i += 1

        return stack

class TestSolution(unittest.TestCase):
    def test_minMeetingRooms(self):
        solution = Solution()
        self.assertEqual(solution.merge([[1, 3],
                                         [2, 6],
                                         [8, 10],
                                         [15, 18]]),
                         [[1, 6],
                          [8, 10],
                          [15, 18]])
        self.assertEqual(solution.merge([[1, 4],
                                         [4, 5]]),
                         [[1, 5]])
        self.assertEqual(solution.merge([[2, 3],
                                         [5, 5],
                                         [2, 2],
                                         [3, 4],
                                         [3, 4]]),
                         [[2, 4], [5, 5]])
        self.assertEqual(solution.merge([[1, 4],
                                         [0, 4]]),
                         [[0, 4]])

if __name__ == '__main__':
    unittest.main()
