#!/usr/bin/env python

import unittest

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not nums:
            return 0.0

        if len(nums) == k:
            return float(sum(nums)) / float(k)

        if k == 1:
            return max(nums)

        _max, _sum = float('-inf'), 0
        for i, num in enumerate(nums):
            if i >= k:
                _max = max(_max, _sum)
                _sum -= nums[i-k]
            _sum += num

        return max(_max, _sum)/float(k)

class TestSolution(unittest.TestCase):
    def test_findMaxAverage(self):
        solution = Solution()
        self.assertEqual(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4), 12.75)
        self.assertEqual(solution.findMaxAverage([1, 12, -5, -6], 4), 0.5)
        self.assertEqual(solution.findMaxAverage([1, 12, -5, -6], 1), 12.0)
        self.assertEqual(solution.findMaxAverage([], 1), 0.0)
        self.assertEqual(solution.findMaxAverage([6, 8, 6, 8, 0, 4, 1, 2, 9, 9], 2), 9.0)


if __name__ == '__main__':
    unittest.main()
