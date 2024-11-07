#!/usr/bin/env python

import unittest


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if not amount:
            return 1

        if not coins:
            return 0

        dp = [[0 for _ in range(len(coins))] for _ in range(amount + 1)]

        for i in range(len(coins)):
            dp[0][i] = 1

        for i in range(1, amount+1):
            for j in range(len(coins)):
                term1 = dp[i][j - 1] if j >= 1 else 0
                term2 = dp[i - coins[j]][j] if i - coins[j] >= 0 else 0
                dp[i][j] = term1 + term2

        return dp[amount][len(coins)-1]


class TestSolution(unittest.TestCase):

    def test_coinChange(self):
        solution = Solution()
        self.assertEqual(solution.change(5, [1, 2, 5]), 4)


if __name__ == '__main__':
    unittest.main()
