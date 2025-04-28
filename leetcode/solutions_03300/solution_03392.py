import unittest


class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        for i in range(n):
            if i + 2 >= n:
                break
            left = i
            mid = i + 1
            right = i + 2
            ans += 1 if (nums[left] + nums[right]) == nums[mid] / 2.0 else 0
        return ans


class TestSolution(unittest.TestCase):
    def test_countSubarrays(self):
        solution = Solution()
        self.assertEqual(solution.countSubarrays([1, 2, 1, 4, 1]), 1)


if __name__ == '__main__':
    unittest.main()
