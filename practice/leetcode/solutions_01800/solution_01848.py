#!/usr/bin/env python3

"""LeetCode solution 01848."""

import unittest


class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        n = len(nums)

        for distance in range(n):
            if start - distance >= 0 and nums[start - distance] == target:
                return distance
            if start + distance < n and distance != 0 and nums[start + distance] == target:
                return distance

        return -1


class TestSolution(unittest.TestCase):
    def test_getMinDistance(self):
        solution = Solution()
        self.assertEqual(solution.getMinDistance([1, 2, 3, 4, 5], 5, 3), 1)
        self.assertEqual(solution.getMinDistance([1], 1, 0), 0)


if __name__ == '__main__':
    unittest.main()
