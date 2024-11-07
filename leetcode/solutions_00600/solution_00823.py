import unittest


class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mod = 10 ** 9 + 7

        arr.sort()

        dp = {x: 1 for x in arr}

        for idx, num in enumerate(arr):
            for j in range(idx):
                if num % arr[j] == 0 and dp.get(num // arr[j]) is not None:
                    dp[num] += dp[arr[j]] * dp[num // arr[j]]

        return sum(dp.values()) % mod


class TestSolution(unittest.TestCase):
    def test_numFactoredBinaryTrees(self):
        solution = Solution()
        self.assertEqual(solution.numFactoredBinaryTrees([2, 4, 5, 10]), 7)


if __name__ == '__main__':
    unittest.main()
