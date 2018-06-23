#!/usr/bin/env python

import unittest

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _sum = sum(nums)
        lsum = 0

        for i, n in enumerate(nums):
            if _sum - n == lsum:
                return i
            else:
                _sum -= n
                lsum += n

        return -1

class TestSolution(unittest.TestCase):
    def test_pivotIndex(self):
        solution = Solution()
        self.assertEqual(solution.pivotIndex([]), -1)
        self.assertEqual(solution.pivotIndex([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(solution.pivotIndex([1, 2, 3]), -1)
        self.assertEqual(solution.pivotIndex([2, 2]), -1)
        self.assertEqual(solution.pivotIndex([-1, -1, -1, -1, -1, 0]), 2)

if __name__ == '__main__':
    unittest.main()
