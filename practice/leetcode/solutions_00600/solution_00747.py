#!/usr/bin/env python3

"""LeetCode solution 00747."""

import unittest

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _max = max(nums)
        idx = -1
        for i, num in enumerate(nums):
            if _max == num:
                idx = i
            if _max != num and num*2 > _max:
                return -1

        return idx

class TestSolution(unittest.TestCase):
    def test_dominantIndex(self):
        solution = Solution()
        self.assertEqual(solution.dominantIndex([3, 6, 1, 0]), 1)
        self.assertEqual(solution.dominantIndex([1, 2, 3, 4]), -1)
        self.assertEqual(solution.dominantIndex([0, 0, 0, 1]), 3)
        self.assertEqual(solution.dominantIndex([1]), 0)
        self.assertEqual(solution.dominantIndex([1, 2]), 1)
        self.assertEqual(solution.dominantIndex([1, 0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()
