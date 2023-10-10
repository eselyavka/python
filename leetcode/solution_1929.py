import unittest


class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)

        ans = [None] * 2 * n
        for i in range(2 * n):
            ans[i] = nums[i % n]

        return ans


class TestSolution(unittest.TestCase):
    def test_getConcatenation(self):
        solution = Solution()
        self.assertListEqual(solution.getConcatenation([1, 2, 1]), [1, 2, 1, 1, 2, 1])


if __name__ == '__main__':
    unittest.main()
