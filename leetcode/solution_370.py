#!/usr/bin/env python

import unittest

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        arr = [0 for _ in range(length)]

        for sidx, eidx, inc in updates:
            arr[sidx] += inc
            if eidx < length - 1:
                arr[eidx+1] -= inc

        for i in range(1, length):
            arr[i] = arr[i] + arr[i-1]

        return arr

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
