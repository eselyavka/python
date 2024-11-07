import unittest


class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        nums.sort()

        ans = -1
        left = 0
        right = n - 1

        while left < right:
            s = nums[left] + nums[right]
            if s < k:
                ans = max(ans, s)
                left += 1
            else:
                right -= 1

        return ans


class TestSolution(unittest.TestCase):
    def test_twoSumLessThanK(self):
        solution = Solution()
        self.assertEqual(solution.twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 60), 58)


if __name__ == '__main__':
    unittest.main()
