#!/usr/bin/env python

import unittest


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        minCoins = [0] + [float('+inf')] * amount
        for j in [c for c in coins if c <= amount]:
            for i in range(1, amount + 1):
                if i >= j:
                    if minCoins[i-j] + 1 < minCoins[i]:
                        minCoins[i] = minCoins[i-j] + 1

        return -1 if minCoins[amount] == float('+inf') else minCoins[amount]


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
