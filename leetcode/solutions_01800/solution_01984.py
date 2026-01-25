import unittest


class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        if n == 1 or k == 1:
            return 0

        i = 0

        ans = float("+inf")
        nums.sort(reverse=True)

        while i <= n - k:
            ans = min(ans, nums[i] - nums[i + k - 1])
            i += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_minimumDifference(self):
        solution = Solution()
        self.assertEqual(solution.minimumDifference([9, 4, 1, 7], 2), 2)


if __name__ == '__main__':
    unittest.main()
