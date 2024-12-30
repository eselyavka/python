import unittest


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        total_sum = sum(nums)
        memo = [[float("-inf")] * (2 * total_sum + 1) for _ in range(n)]

        def rec(i, curr_sum, memo):
            if curr_sum == target and i == len(nums):
                return 1

            if i >= len(nums):
                return 0

            if memo[i][curr_sum + total_sum] != float("-inf"):
                return memo[i][curr_sum + total_sum]

            add = rec(i + 1, curr_sum + nums[i], memo)
            subtract = rec(i + 1, curr_sum - nums[i], memo)
            memo[i][curr_sum + total_sum] = add + subtract

            return memo[i][curr_sum + total_sum]

        return rec(0, 0, memo)


class TestSolution(unittest.TestCase):
    def test_findTargetSumWays(self):
        solution = Solution()

        self.assertEqual(solution.findTargetSumWays([1, 1, 1, 1, 1], 3), 5)


if __name__ == '__main__':
    unittest.main()
