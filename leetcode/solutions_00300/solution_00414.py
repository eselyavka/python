#!/usr/bin/env python

import unittest


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        _max, sec, third = float('-inf'), float('-inf'), float('-inf')

        for num in nums:
            if num > _max:
                third = sec
                sec = _max
                _max = num
            elif num < _max and num > sec:
                third = sec
                sec = num
            elif num < sec and num > third:
                third = num

        return third if third != float('-inf') else _max

    def thirdMax2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, third = [float('-inf')] * 3
        i = 0

        while i < len(nums):
            if nums[i] > first:
                third = second
                second = first
                first = nums[i]
            elif nums[i] > second and nums[i] != first:
                third = second
                second = nums[i]
            elif nums[i] > third and nums[i] != first and nums[i] != second:
                third = nums[i]

            i += 1

        return third if third != float('-inf') else first


class TestSolution(unittest.TestCase):

    def test_thirdMax(self):

        solution = Solution()

        self.assertEqual(solution.thirdMax([1, 2, 3, 1]), 1)
        self.assertEqual(solution.thirdMax([1, 2]), 2)
        self.assertEqual(solution.thirdMax([2, 2, 3, 1]), 1)
        self.assertEqual(solution.thirdMax([1, 0, 1, 1]), 1)
        self.assertEqual(solution.thirdMax([1, 2, 3, 1, 2, 3]), 1)
        self.assertEqual(solution.thirdMax([1, -2147483648, 2]), -2147483648)

        self.assertEqual(solution.thirdMax2([1, 2, 3, 1]), 1)
        self.assertEqual(solution.thirdMax2([1, 2]), 2)
        self.assertEqual(solution.thirdMax2([2, 2, 3, 1]), 1)
        self.assertEqual(solution.thirdMax2([1, 0, 1, 1]), 1)
        self.assertEqual(solution.thirdMax2([1, 2, 3, 1, 2, 3]), 1)
        self.assertEqual(solution.thirdMax2([1, -2147483648, 2]), -2147483648)


if __name__ == '__main__':
    unittest.main()
