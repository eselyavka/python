#!/usr/bin/env python

import unittest


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def is_even(num):
            if num < 9:
                return False

            nums = []
            while num:
                nums.append(num % 10)
                num = num // 10

            return len(nums) % 2 == 0

        res = 0
        for num in nums:
            if is_even(num):
                res += 1

        return res


class TestSolution(unittest.TestCase):
    def test_findNumbers(self):
        solution = Solution()
        self.assertEqual(solution.findNumbers([12, 345, 2, 6, 7896]), 2)


if __name__ == '__main__':
    unittest.main()
