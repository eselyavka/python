#!/usr/bin/env python

import unittest

class Solution(object):
    def dp(self, coins, amount, minCoins):
        for j in [c for c in coins if c <= amount]:
            for i in range(1, amount + 1):
                if i >= j:
                    if minCoins[i-j] + 1 < minCoins[i]:
                        minCoins[i] = minCoins[i-j] + 1

        return minCoins[amount]

    def _rec(self, coins, amount, memo):
        if not amount:
            return 0

        if amount in coins:
            memo[amount] = 1
            return 1

        if memo.has_key(amount):
            return memo[amount]

        min_coins = float('+inf')

        for i in [c for c in coins if c < amount]:
            num_coins = 1 + self._rec(coins, amount - i, memo)
            if num_coins < min_coins:
                min_coins = num_coins

        memo[amount] = min_coins

        return min_coins

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = self.dp(coins, amount, [0] + [float('inf')]*amount)

        return res if res != float('+inf') else -1

class TestSolution(unittest.TestCase):

    def test_coinChange(self):
        solution = Solution()
        self.assertEqual(solution.coinChange([1, 2, 5], 100), 20)
        self.assertEqual(solution.coinChange([1, 2, 5], 11), 3)
        self.assertEqual(solution.coinChange([1, 5, 10, 25], 63), 6)
        self.assertEqual(solution.coinChange([1], 0), 0)
        self.assertEqual(solution.coinChange([2], 4), 2)
        self.assertEqual(solution.coinChange([2], 7), -1)
        self.assertEqual(solution.coinChange([2147483647], 2), -1)
        self.assertEqual(solution.coinChange([186, 419, 83, 408], 6249), 20)
        self.assertEqual(solution.coinChange([333, 364, 408, 118, 63, 270,
                                              69, 111, 218, 371, 305], 5615), 15)

if __name__ == '__main__':
    unittest.main()
