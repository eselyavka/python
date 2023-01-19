#!/usr/bin/env python

import unittest


class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        ans = [0] * length

        for sidx, eidx, inc in updates:
            ans[sidx] += inc
            if eidx < length - 1:
                ans[eidx + 1] -= inc

        for i in range(1, length):
            ans[i] += ans[i - 1]

        return ans


class TestSolution(unittest.TestCase):

    def test_getModifiedArray(self):
        length = 5
        updates = [[1, 3, 2],
                   [2, 4, 3],
                   [0, 2, -2]]

        solution = Solution()
        self.assertEqual(solution.getModifiedArray(length, updates), [-2, 0, 3, 5, 3])


if __name__ == '__main__':
    unittest.main()
