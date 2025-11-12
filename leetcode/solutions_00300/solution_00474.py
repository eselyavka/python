import unittest


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            z = s.count("0")
            o = s.count("1")

            if z > m or o > n:
                continue

            for i in range(m, z - 1, -1):
                for j in range(n, o - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - z][j - o] + 1)

        return dp[-1][-1]


class TestSolution(unittest.TestCase):
    def test_findMaxForm(self):
        solution = Solution()
        self.assertEqual(solution.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3), 4)


if __name__ == '__main__':
    unittest.main()
