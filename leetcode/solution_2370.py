import unittest


class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        n = len(s)
        if n == 1:
            return 1

        def in_range(dp, l, r):
            cnt = 0

            for i in range(l, r + 1):
                cnt = max(cnt, dp[i])

            return cnt

        dp = [0 for _ in range(26)]

        for c in s:
            i = ord(c) - ord("a")
            dp[i] = 1 + in_range(dp, max(0, i - k), min(25, i + k))

        return max(dp)


class TestSolution(unittest.TestCase):
    def test_longestIdealString(self):
        solution = Solution()
        self.assertEqual(solution.longestIdealString("acfgbd", 2), 4)


if __name__ == '__main__':
    unittest.main()
