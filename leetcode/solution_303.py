#!/usr/bin/env python

import unittest

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self._nums = [0 for _ in range(len(nums)+1)]

        for i, num in enumerate(nums):
            self._nums[i+1] = num + self._nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        return self._nums[j+1] - self._nums[i]

class TestSolution(unittest.TestCase):

    def test_NumArray(self):
        solution = NumArray([-2, 0, 3, -5, 2, -1])

        self.assertEqual(solution.sumRange(0, 2), 1)
        self.assertEqual(solution.sumRange(2, 5), -1)
        self.assertEqual(solution.sumRange(0, 5), -3)

if __name__ == '__main__':
    unittest.main()
