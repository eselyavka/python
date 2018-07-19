#!/usr/bin/env python

import unittest

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        arr = sorted(nums, reverse=True)
        d = {t[0]:t[1] for t in zip(arr[:3],
                                    ["Gold Medal", "Silver Medal", "Bronze Medal"])}
        d.update({t[1]:str(t[0]+4) for t in enumerate(arr[3:])})

        for i, num in enumerate(nums):
            nums[i] = d[num]

        return nums

class TestSolution(unittest.TestCase):
    def test_findRelativeRanks(self):
        solution = Solution()
        self.assertEqual(solution.findRelativeRanks([5, 4, 3, 2, 1]),
                         ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"])
        self.assertEqual(solution.findRelativeRanks([10, 3, 8, 9, 4]),
                         ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"])

if __name__ == '__main__':
    unittest.main()
