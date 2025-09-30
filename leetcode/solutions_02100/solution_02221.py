import unittest


class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        while len(nums) != 1:
            n = len(nums)
            for i in range(1, n):
                nums[i - 1] = (nums[i - 1] + nums[i]) % 10
            nums.pop()

        return nums[0]


class TestSolution(unittest.TestCase):
    def test_triangularSum(self):
        solution = Solution()
        self.assertEqual(solution.triangularSum([1, 2, 3, 4, 5]), 8)


if __name__ == '__main__':
    unittest.main()
