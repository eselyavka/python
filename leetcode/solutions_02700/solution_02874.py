import unittest


class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        leftMax = [0] * n
        rightMax = [0] * n

        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], nums[i - 1])
            rightMax[n - i - 1] = max(rightMax[n - i], nums[n - i])
        ans = 0
        for j in range(1, n - 1):
            ans = max(ans, (leftMax[j] - nums[j]) * rightMax[j])

        return ans


class TestSolution(unittest.TestCase):
    def test_maximumTripletValue(self):
        solution = Solution()
        self.assertEqual(solution.maximumTripletValue([12, 6, 1, 2, 7]), 77)


if __name__ == '__main__':
    unittest.main()
