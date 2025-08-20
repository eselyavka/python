#!/usr/bin/env python

import unittest


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])

        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        ans = 0

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    ans += dp[i][j]

        return ans


class TestSolution(unittest.TestCase):
    def test_countSquares(self):
        solution = Solution()
        self.assertEqual(solution.countSquares([[0, 1, 1, 1],
                                                [1, 1, 1, 1],
                                                [0, 1, 1, 1]]), 15)


if __name__ == '__main__':
    unittest.main()
