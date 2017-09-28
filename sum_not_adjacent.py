#!/usr/bin/env python

import unittest

class Solution(object):
    def sum_not_adjacent2(self, arr, idx=0):
        print "sum_not_adjacent2 has been called with and idx = {}".format(idx)
        if idx >= len(arr):
            return 0

        v1 = arr[idx] + self.sum_not_adjacent2(arr, idx + 2)
        v2 = self.sum_not_adjacent2(arr, idx + 1)
        print "intermediate result for ", v1, " and ",v2,
        return v1 if v1 > v2 else v2

    def sum_not_adjacent(self, arr, sums=None):
        """
        :type arr: List[int]
        :rtype: int
        """

        if sums is None:
            sums = list()

        if not arr:
            return max(sums)
        
        sums.append()
        return self.sum_not_adjacent(arr[1:], sums)

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.arr1 = [5, 1, 2, 6, 20, 2]
        self.arr2 = [53, 1, 12, 65, 200, 2, 7, 90, 100, 54]
        self.arr3 = [1, 2, 3, 4]
        self.arr4 = [1, 1, 1, 1]

    def test_matrixReshape(self):
        solution = Solution()
        #self.assertEqual(solution.sum_not_adjacent(self.arr1), 27)
        self.assertEqual(solution.sum_not_adjacent2(self.arr2), 372)
        #self.assertEqual(solution.sum_not_adjacent(self.arr3), 6)
        #self.assertEqual(solution.sum_not_adjacent(self.arr4), 1)

if __name__ == '__main__':
    unittest.main()
