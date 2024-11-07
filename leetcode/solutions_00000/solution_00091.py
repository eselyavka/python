import unittest


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.startswith("0"):
            return 0

        n = len(s)
        dp = [None for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = 0

            if s[i - 1] > '0':
                dp[i] = dp[i - 1]

            if (s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] < '7')):
                dp[i] += dp[i - 2]

        return dp[n]


class TestSolution(unittest.TestCase):
    def test_numDecodings(self):
        solution = Solution()
        self.assertEqual(solution.numDecodings("112"), 3)


if __name__ == '__main__':
    unittest.main()
