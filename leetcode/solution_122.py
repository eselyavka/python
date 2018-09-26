#!/usr/bin/env python

import unittest

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) in [0, 1]:
            return 0

        if len(prices) == 2:
            return prices[1] - prices[0] if prices[1] > prices[0] else 0

        res, i = 0, 0
        mas = []
        while i < len(prices):
            while i < len(prices) - 1 and prices[i+1] <= prices[i]:
                i += 1
            if i == len(prices) - 1:
                break

            _int = [i]
            i += 1

            while i < len(prices) and prices[i-1] <= prices[i]:
                i += 1

            _int.append(i-1)

            mas.append(_int)

        for buy, sell in mas:
            res += prices[sell] - prices[buy]

        return res

class TestSolution(unittest.TestCase):

    def test_maxProfit(self):
        solution = Solution()

        self.assertEqual(solution.maxProfit([7, 1, 5, 3, 6, 4]), 7)
        self.assertEqual(solution.maxProfit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(solution.maxProfit([1, 2, 3, 4, 5]), 4)

if __name__ == '__main__':
    unittest.main()
