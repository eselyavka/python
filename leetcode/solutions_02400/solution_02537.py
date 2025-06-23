import unittest
from collections import defaultdict


class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        d = defaultdict(int)
        running_pairs = 0
        ans = 0
        r = 0

        for l in range(n):
            while r < n and running_pairs < k:
                x = nums[r]
                running_pairs += d[x]
                d[x] += 1
                r += 1

            if running_pairs < k:
                break

            ans += (n - r + 1)

            y = nums[l]
            d[y] -= 1
            running_pairs -= d[y]

        return ans


class TestSolution(unittest.TestCase):
    def test_countGood(self):
        solution = Solution()
        self.assertEqual(solution.countGood([3, 1, 4, 3, 2, 2, 4], 2), 4)


if __name__ == '__main__':
    unittest.main()
