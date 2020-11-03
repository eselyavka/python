#!/usr/bin/env python

import unittest


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2:
            return False

        half = total / 2
        n = len(nums)
        dp = [[False for _ in range(half + 1)] for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            curr = nums[i-1]
            for j in range(1, half + 1):
                if j < curr:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-curr]

        return dp[n][half]


class TestSolution(unittest.TestCase):
    def test_canPartition(self):
        solution = Solution()
        self.assertTrue(solution.canPartition([1, 5, 11, 5]))


if __name__ == '__main__':
    unittest.main()
