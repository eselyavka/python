#!/usr/bin/env python

import unittest


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals or len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda l: l[0])
        stack = [intervals[0]]

        i = 1
        while i < len(intervals):
            interval = stack.pop()
            end_prev = interval[1]
            start_curr = intervals[i][0]
            if end_prev >= start_curr:
                start_prev = interval[0]
                end_curr = intervals[i][1]
                stack.append([min(start_prev, start_curr),
                              max(end_prev, end_curr)])
            else:
                stack.append(interval)
                stack.append(intervals[i])
            i += 1

        return stack


class Solution2(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals or len(intervals) == 1:
            return intervals

        res = sorted(intervals, key=lambda l: l[0])

        i = 1
        while i < len(res):
            end_prev = res[i-1][1]
            start_curr = res[i][0]
            if end_prev >= start_curr:
                start_prev = res[i-1][0]
                end_curr = res[i][1]
                res[i][0] = min(start_prev, start_curr)
                res[i][1] = max(end_prev, end_curr)
                del res[i-1]
                continue
            i += 1
        return res


class TestSolution(unittest.TestCase):
    def test_merge(self):
        solution = Solution()
        self.assertListEqual(solution.merge([[1, 3],
                                             [2, 6],
                                             [8, 10],
                                             [15, 18]]),
                             [[1, 6],
                              [8, 10],
                              [15, 18]])
        self.assertListEqual(solution.merge([[1, 4],
                                             [4, 5]]),
                             [[1, 5]])
        self.assertListEqual(solution.merge([[2, 3],
                                             [5, 5],
                                             [2, 2],
                                             [3, 4],
                                             [3, 4]]),
                             [[2, 4], [5, 5]])
        self.assertListEqual(solution.merge([[1, 4],
                                             [0, 4]]),
                             [[0, 4]])

        solution2 = Solution2()
        self.assertListEqual(solution2.merge([[1, 4],
                                              [0, 2],
                                              [3, 5]]),
                             [[0, 5]])


if __name__ == '__main__':
    unittest.main()
