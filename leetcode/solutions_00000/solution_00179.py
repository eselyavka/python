#!/usr/bin/env python

import unittest

def comparator(a, b):
    _a = str(a)+str(b)
    _b = str(b) + str(a)
    return cmp(int(_a), int(_b))

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ''

        if len(nums) == 1:
            return str(nums[0])

        mas = sorted(nums, cmp=comparator, reverse=True)
        res = ''.join([str(x) for x in mas]) if mas[0] > 0 else '0'
        return res

class TestSolution(unittest.TestCase):

    def test_largestNumber(self):

        solution = Solution()

        self.assertEqual(solution.largestNumber([10, 2]), "210")
        self.assertEqual(solution.largestNumber([0, 0]), "0")
        self.assertEqual(solution.largestNumber([3, 30, 34, 5, 9]), "9534330")
        self.assertEqual(solution.largestNumber([74, 21, 33, 51, 77, 51, 90, 60, 5, 56]),
                         "9077746056551513321")

if __name__ == '__main__':
    unittest.main()
