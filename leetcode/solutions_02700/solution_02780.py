import unittest
from collections import Counter


class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        counter = Counter(nums)
        max_occur = float("-inf")
        x = -1
        for k, v in counter.items():
            if v > max_occur:
                max_occur = v
                x = k

        left_occur = 0
        for i in range(n):
            if nums[i] == x:
                max_occur -= 1
                left_occur += 1
                if left_occur > ((i + 1) - left_occur) and max_occur > (n - (i + 1) - max_occur):
                    return i

        return -1


class TestSolution(unittest.TestCase):
    def test_minimumIndex(self):
        solution = Solution()
        self.assertEqual(solution.minimumIndex([1, 2, 2, 2]), 2)


if __name__ == '__main__':
    unittest.main()
