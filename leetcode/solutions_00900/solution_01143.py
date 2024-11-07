import unittest


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                if text2[j] == text1[i]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


class TestSolution(unittest.TestCase):
    def test_longestCommonSubsequence(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonSubsequence("abcde", "ace"), 3)


if __name__ == '__main__':
    unittest.main()
