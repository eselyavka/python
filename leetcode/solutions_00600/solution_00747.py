#!/usr/bin/env python

import unittest

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _max = max(nums)
        idx = -1
        for i in range(len(nums)):
            if _max == nums[i]:
                idx = i
            if _max != nums[i] and nums[i]*2 > _max:
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
