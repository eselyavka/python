#!/usr/bin/env python

import unittest


class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0] * 366
        days_set = set(days)

        for day in range(1, 366):
            if day in days_set:
                dp[day] = min(dp[day-1] + costs[0],
                              dp[max(0, day-7)] + costs[1],
                              dp[max(0, day-30)] + costs[2])
            else:
                dp[day] = dp[day-1]

        return dp[365]


class TestSolution(unittest.TestCase):
    def test_mincostTickets(self):
        solution = Solution()
        self.assertEqual(solution.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]), 11)


if __name__ == '__main__':
    unittest.main()
