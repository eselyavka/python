#!/usr/bin/env python

import unittest

class Solution(object):
    def _rob(self, nums):

        dp = [0] * len(nums)
        res = 0
        for i in range(len(nums)):
            res = max(nums[i]+(dp[i-2] if i >= 2 else 0), (dp[i-1] if i > 0 else 0))
            dp[i] = res

        return res

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        return max(self._rob(nums[:-1]), self._rob(nums[1:]))

class TestSolution(unittest.TestCase):

    def test_rob(self):
        solution = Solution()

        self.assertEqual(solution.rob([2, 3, 2]), 3)
        self.assertEqual(solution.rob([1, 2, 3, 1]), 4)

if __name__ == '__main__':
    unittest.main()
