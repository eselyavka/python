import sys
import unittest


class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """

        def rec(memo, i, j):
            if i + 1 == j:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            res = sys.maxsize

            for k in range(i + 1, j):
                curr = rec(memo, i, k) + rec(memo, k, j) + values[i] * values[j] * values[k]
                res = min(res, curr)

            memo[i][j] = res

            return res

        n = len(values)
        memo = [[-1 for _ in range(n)] for _ in range(n)]

        res = rec(memo, 0, n - 1)

        return res


class TestSolution(unittest.TestCase):
    def test_minScoreTriangulation(self):
        solution = Solution()
        self.assertEqual(solution.minScoreTriangulation([3, 7, 4, 5]), 144)


if __name__ == '__main__':
    unittest.main()
