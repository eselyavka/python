import unittest


class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        right = 0
        left = 0
        ans = 0

        while right < n:
            if nums[right] == 1 or nums[right] == 0 and k > 0:
                if nums[right] == 0:
                    k -= 1
                right += 1
            else:
                ans = max(ans, right - left)
                while k == 0:
                    if nums[left] == 0: k += 1
                    left += 1

            ans = max(ans, right - left)

        return ans


class TestSolution(unittest.TestCase):
    def test_longestOnes(self):
        solution = Solution()
        self.assertEqual(solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6)


if __name__ == '__main__':
    unittest.main()
