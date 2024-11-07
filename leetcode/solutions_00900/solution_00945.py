import unittest
from collections import Counter


class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        ans = 0
        if n == 1:
            return ans

        counter = Counter(nums)

        taken = []
        for i in range(n + max(nums)):
            if counter[i] > 1:
                taken.extend([i] * (counter[i] - 1))
            elif taken and counter[i] == 0:
                ans += i - taken.pop()
        return ans


class TestSolution(unittest.TestCase):
    def test_minIncrementForUnique(self):
        solution = Solution()
        self.assertEqual(solution.minIncrementForUnique([3,2,1,2,1,7]), 6)


if __name__ == '__main__':
    unittest.main()
