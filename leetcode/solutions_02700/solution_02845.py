import unittest
from collections import defaultdict


class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        m = defaultdict(int)
        m[0] += 1
        ans, prefix = 0, 0
        for i in range(n):
            prefix += (1 if nums[i] % modulo == k else 0)
            ans += m[(prefix + modulo - k) % modulo]
            m[prefix % modulo] += 1
        return ans


class TestSolution(unittest.TestCase):
    def test_countInterestingSubarrays(self):
        solution = Solution()
        self.assertEqual(solution.countInterestingSubarrays([3, 2, 4], 2, 1), 3)


if __name__ == '__main__':
    unittest.main()
