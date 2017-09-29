#!/usr/bin/env python

import unittest

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        excl = 0
        incl = 0
        for i in nums:
            new_excl = max(excl, incl)
            incl = excl + i
            excl = new_excl

        return max(excl, incl)

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.arr1 = [5, 1, 2, 6, 20, 2]
        self.arr2 = [53, 1, 12, 65, 200, 2, 7, 90, 100, 54]
        self.arr3 = [1, 2, 3, 4]
        self.arr4 = [1, 1, 1, 1]
        self.arr5 = [1, 3, 1]
        self.arr6 = [2, 1, 1, 2]

    def test_matrixReshape(self):
        solution = Solution()
        self.assertEqual(solution.rob(self.arr1), 27)
        self.assertEqual(solution.rob(self.arr2), 409)
        self.assertEqual(solution.rob(self.arr3), 6)
        self.assertEqual(solution.rob(self.arr4), 2)
        self.assertEqual(solution.rob(self.arr5), 3)
        self.assertEqual(solution.rob(self.arr6), 4)

if __name__ == '__main__':
    unittest.main()
