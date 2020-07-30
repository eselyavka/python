#!/usr/bin/env python

import unittest


class Solution(object):
    def cum_sum(self, arr, i, n):
        cumulative_sum = [None] * (n - i)
        cumulative_sum[0] = arr[i]

        for j in range(1, n-i):
            cumulative_sum[j] = cumulative_sum[j-1]+arr[i+j]

        return cumulative_sum

    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        res = []
        for i in range(n):
            res += self.cum_sum(nums, i, n)

        res.sort()

        sum_ = 0

        for i in range(left-1, right):
            sum_ += res[i]

        return sum_ % (10**9 + 7)


class TestSolution(unittest.TestCase):
    def test_rangeSum(self):
        solution = Solution()
        self.assertEqual(solution.rangeSum([1, 2, 3, 4], 4, 1, 5), 13)


if __name__ == '__main__':
    unittest.main()
