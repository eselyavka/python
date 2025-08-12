import unittest


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        dp = [[num] for num in nums]

        res = []
        for j in range(n - 1, -1, -1):
            for k in range(j + 1, n):
                if nums[k] % nums[j] == 0:
                    tmp = [nums[j]] + dp[k]
                    dp[j] = tmp if len(tmp) > len(dp[j]) else dp[j]
            res = dp[j] if len(dp[j]) > len(res) else res

        return res if res else dp[0]


class TestSolution(unittest.TestCase):
    def test_largestDivisibleSubset(self):
        solution = Solution()
        self.assertEqual(solution.largestDivisibleSubset([4, 8, 10, 240]), [4, 8, 240])


if __name__ == '__main__':
    unittest.main()
