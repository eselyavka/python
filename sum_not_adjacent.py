#!/usr/bin/env python

import unittest

class Solution(object):
    def sum_not_adjacent(self, arr, sums=None):
        """
        :type arr: List[int]
        :rtype: int
        """

        if sums is None:
            sums = list()

        if not arr:
            return max(sums)

        sums.append(sum(set(arr[::2])))
        return self.sum_not_adjacent(arr[1:], sums)

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.arr1 = [5, 1, 2, 6, 20, 2]
        self.arr2 = [53, 1, 12, 65, 200, 2, 7, 90, 100, 54]
        self.arr3 = [1, 2, 3, 4]
        self.arr4 = [1, 1, 1, 1]

    def test_matrixReshape(self):
        solution = Solution()
        self.assertEqual(solution.sum_not_adjacent(self.arr1), 27)
        self.assertEqual(solution.sum_not_adjacent(self.arr2), 372)
        self.assertEqual(solution.sum_not_adjacent(self.arr3), 6)
        self.assertEqual(solution.sum_not_adjacent(self.arr4), 1)

if __name__ == '__main__':
    unittest.main()
