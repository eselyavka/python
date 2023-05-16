import unittest


class Solution(object):
    def minimizeArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = prefix_sum = 0
        for idx, num in enumerate(nums):
            prefix_sum += num
            ans = max(ans, (prefix_sum + idx) / (idx + 1))

        return int(ans)


class TestSolution(unittest.TestCase):
    def test_minimizeArrayValue(self):
        solution = Solution()
        self.assertEqual(solution.minimizeArrayValue([3, 7, 1, 6]), 5)


if __name__ == '__main__':
    unittest.main()
