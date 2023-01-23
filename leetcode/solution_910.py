import unittest


class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        ans = nums[-1] - nums[0]
        left = nums[0] + k
        right = nums[-1] - k
        for i in range(n - 1):
            max_ = max(nums[i] + k, right)
            min_ = min(nums[i + 1] - k, left)
            ans = min(ans, max_ - min_)

        return ans


class TestSolution(unittest.TestCase):
    def test_smallestRangeII(self):
        solution = Solution()
        self.assertEqual(solution.smallestRangeII([1, 3, 6], 3), 3)


if __name__ == '__main__':
    unittest.main()
