import unittest
from collections import Counter


class Solution(object):
    def subarraysWithMoreZerosThanOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        c = Counter({0: 1})
        ans, dp, s = 0, 0, 0

        for num in nums:
            if num:
                s += 1
                dp += c[s - 1]
            else:
                s -= 1
                dp -= c[s]
            ans += dp
            c[s] += 1
        return ans % (10 ** 9 + 7)


class TestSolution(unittest.TestCase):
    def test_subarraysWithMoreZerosThanOnes(self):
        solution = Solution()
        self.assertEqual(solution.subarraysWithMoreZerosThanOnes([0, 1, 1, 0, 1]), 9)


if __name__ == '__main__':
    unittest.main()
