#!/usr/bin/env python

import unittest

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        _min = prices[0]
        maxprofit = 0

        for i in range(len(prices)):
            if _min >= prices[i]:
                _min = prices[i]
            elif prices[i] - _min > maxprofit:
                maxprofit = prices[i] - _min

        return maxprofit


class TestSolution(unittest.TestCase):

    def test_maxProfit(self):
        arr = [7, 1, 5, 3, 6, 4]
        arr2 = [7, 6, 4, 3, 1]
        arr3 = []
        arr4 = [1]
        arr5 = [6, 1]
        arr6 = [2, 4, 1]
        arr7 = [2, 4, 1, 6]
        arr8 = [2, 4, 6, 1]
        arr9 = [3, 2, 6, 5, 0, 3]
        solution = Solution()
        self.assertEqual(solution.maxProfit(arr), 5)
        self.assertEqual(solution.maxProfit(arr2), 0)
        self.assertEqual(solution.maxProfit(arr3), 0)
        self.assertEqual(solution.maxProfit(arr4), 0)
        self.assertEqual(solution.maxProfit(arr5), 0)
        self.assertEqual(solution.maxProfit(arr6), 2)
        self.assertEqual(solution.maxProfit(arr7), 5)
        self.assertEqual(solution.maxProfit(arr8), 4)
        self.assertEqual(solution.maxProfit(arr9), 4)

if __name__ == '__main__':
    unittest.main()
