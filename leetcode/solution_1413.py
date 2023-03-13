import unittest


class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = float("-inf")

        sum_so_far = 0
        for num in nums:
            sum_so_far += num
            if sum_so_far <= 0:
                x = -sum_so_far + 1
                ans = max(ans, x)

        return ans if ans != float("-inf") else 1


class TestSolution(unittest.TestCase):
    def test_minStartValue(self):
        solution = Solution()
        self.assertEqual(solution.minStartValue([-3, 2, -3, 4, 2]), 5)


if __name__ == '__main__':
    unittest.main()
