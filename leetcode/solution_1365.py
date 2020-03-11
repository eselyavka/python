#!/usr/bin/env python

import unittest


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        _nums = sorted(nums)
        d = dict()
        d[_nums[0]] = 0

        for i in range(1, len(nums)):
            if _nums[i] not in d:
                if _nums[i] > _nums[i-1]:
                    d[_nums[i]] = i
                else:
                    d[_nums[i]] = 0
        res = []
        for num in nums:
            res.append(d[num])

        return res


class TestSolution(unittest.TestCase):

    def test_smallerNumbersThanCurrent(self):
        solution = Solution()
        self.assertListEqual(
            solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]),
            [4, 0, 1, 1, 3])


if __name__ == '__main__':
    unittest.main()
