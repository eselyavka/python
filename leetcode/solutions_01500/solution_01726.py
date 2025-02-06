#!/usr/bin/env python

import unittest

from collections import defaultdict


class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        n = len(nums)

        products = defaultdict(set)
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                if nums[i] != nums[j]:
                    products[product] |= {nums[i], nums[j]}
        ans = 0
        for product in products:
            t_len = len(products[product])
            if t_len >= 4:
                ans += t_len * (t_len - 2)

        return ans


class TestSolution(unittest.TestCase):
    def test_tupleSameProduct(self):
        solution = Solution()
        self.assertEqual(solution.tupleSameProduct([2, 3, 4, 6, 8, 12]), 40)


if __name__ == '__main__':
    unittest.main()
