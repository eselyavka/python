import unittest
from collections import Counter


class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            return int(nums[0] % k == 0)

        ans = 0
        running_sum = 0
        c = Counter()

        for num in nums:
            running_sum += num
            if running_sum % k == 0:
                ans += 1

            ans += c[running_sum % k]

            c[running_sum % k] += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_subarraysDivByK(self):
        solution = Solution()
        self.assertEqual(solution.subarraysDivByK([4, 5, 0, -2, -3, 1], 5), 7)
        self.assertEqual(solution.subarraysDivByK([2, -2, 2, -4], 6), 2)


if __name__ == '__main__':
    unittest.main()
