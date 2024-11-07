import unittest


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return True

        dp = [False for i in range(n)]
        goal = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= goal:
                dp[i] = True
                goal = i

        return dp[0]


class TestSolution(unittest.TestCase):
    def test_canJump(self):
        solution = Solution()
        self.assertTrue(solution.canJump([2, 3, 1, 1, 4]))


if __name__ == '__main__':
    unittest.main()
