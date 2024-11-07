import math
import unittest


class Solution(object):
    def subarrayLCM(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        ans = 0
        for i in range(n):
            curr = nums[i]
            if curr == k:
                ans += 1
            for j in range(i + 1, n):
                curr = math.lcm(curr, nums[j])
                if curr == k:
                    ans += 1
                if curr > k:
                    break

        return ans


class TestSolution(unittest.TestCase):
    def test_subarrayLCM(self):
        solution = Solution()
        self.assertEqual(solution.subarrayLCM([3, 6, 2, 7, 1], 6), 4)


if __name__ == '__main__':
    unittest.main()
