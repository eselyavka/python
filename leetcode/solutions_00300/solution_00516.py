import unittest


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        rev = s[::-1]

        n = len(s)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == rev[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


class TestSolution(unittest.TestCase):
    def test_longestPalindromeSubseq(self):
        solution = Solution()
        self.assertEqual(solution.longestPalindromeSubseq("bbbab"), 4)


if __name__ == '__main__':
    unittest.main()
