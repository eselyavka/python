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

        half = total // 2
        n = len(nums)
        dp = [[False for _ in range(half + 1)] for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(1, half + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]

        return dp[n][half]


class Solution2(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        n = len(nums)
        memo = dict()

        def rec(idx, running_sum):
            if idx >= n or running_sum < 0:
                return False
            if running_sum == 0:
                return True

            key = (idx, running_sum)
            if key in memo:
                return memo[key]

            if rec(idx + 1, running_sum - nums[idx]) or rec(idx + 1, running_sum):
                memo[key] = True
            else:
                memo[key] = False

            return memo[key]

        if total_sum % 2 != 0:
            return False

        return rec(0, total_sum / 2)


class TestSolution(unittest.TestCase):
    def test_canPartition(self):
        solution = Solution()
        self.assertTrue(solution.canPartition([1, 5, 11, 5]))
        solution2 = Solution2()
        self.assertTrue(solution2.canPartition([1, 5, 11, 5]))


if __name__ == '__main__':
    unittest.main()
