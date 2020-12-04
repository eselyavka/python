#!/usr/bin/env python

import unittest


class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        arr = []
        for p in points:
            arr.append(p[0])
        arr.sort()

        res = 0
        for i in range(1, len(arr)):
            res = max(res, arr[i]-arr[i-1])

        return res


class TestSolution(unittest.TestCase):

    def test_maxWidthOfVerticalArea(self):
        solution = Solution()
        self.assertEqual(solution.maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]), 1)


if __name__ == '__main__':
    unittest.main()
