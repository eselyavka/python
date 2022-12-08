import unittest


class Solution(object):
    def minimumSplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def gcd(a, b):
            if a == 0:
                return b

            return gcd(b % a, a)

        n = len(nums)
        ans, curr = 1, nums[0]
        for i in range(1, n):
            curr = gcd(curr, nums[i])
            if curr == 1:
                ans += 1
                curr = nums[i]
        return ans


class TestSolution(unittest.TestCase):
    def test_minimumSplits(self):
        solution = Solution()
        self.assertEqual(solution.minimumSplits([12, 6, 3, 14, 8]), 2)


if __name__ == '__main__':
    unittest.main()
