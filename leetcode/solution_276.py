#!/usr/bin/env python

import unittest


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        dp = [0, k, k**2, 0]

        if n <= 2:
            return dp[n]

        for _ in range(2, n):
            dp[3] = (k-1) * (dp[1] + dp[2])
            dp[1] = dp[2]
            dp[2] = dp[3]

        return dp[3]


class TestSolution(unittest.TestCase):
    def test_numWays(self):
        solution = Solution()
        self.assertEqual(solution.numWays(3, 2), 6)
        self.assertEqual(solution.numWays(2, 4), 16)
        self.assertEqual(solution.numWays(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
