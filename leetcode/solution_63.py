import unittest
from itertools import product


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = int(obstacleGrid[0][0] == 0)

        for i, j in product(range(m), range(n)):
            if obstacleGrid[i][j] == 1:
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]

        return dp[m - 1][n - 1]


class TestSolution(unittest.TestCase):
    def test_uniquePathsWithObstacles(self):
        solution = Solution()
        self.assertEqual(solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)


if __name__ == '__main__':
    unittest.main()
