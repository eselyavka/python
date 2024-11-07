import unittest


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]

        curr_min, curr_max = 1, 1

        for num in nums:
            product_max = num * curr_max
            product_min = num * curr_min
            curr_max = max(product_max, product_min, num)
            curr_min = min(product_min, product_min, num)
            ans = max(ans, curr_max)

        return ans


class TestSolution(unittest.TestCase):
    def test_maxProduct(self):
        solution = Solution()
        self.assertEqual(solution.maxProduct([-2,3,-4]), 24)


if __name__ == '__main__':
    unittest.main()
