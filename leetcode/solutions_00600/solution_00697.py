#!/usr/bin/env python

import unittest

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return []

        d = {}
        for i, num in enumerate(nums):
            if num in d:
                d[num][0] += 1
                d[num][1][1] = i
            else:
                d[num] = [1, [i, i+1]]

        if len(nums) == len(d.keys()):
            return 1

        sd = sorted(d.iteritems(), key=lambda x: x[1][0], reverse=True)
        res = sd[0]

        for i in sd:
            if res[1][0] > i[1][0]:
                return (res[1][1][1] - res[1][1][0]) + 1
            else:
                if (res[1][1][1] - res[1][1][0])+1 > (i[1][1][1] - i[1][1][0]) + 1:
                    res = i

        return (res[1][1][1] - res[1][1][0]) + 1

class TestSolution(unittest.TestCase):

    def test_findShortestSubArray(self):

        solution = Solution()

        self.assertEqual(solution.findShortestSubArray([1, 2, 2, 3, 1]), 2)
        self.assertEqual(solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]), 6)
        self.assertEqual(solution.findShortestSubArray([1, 2, 5, 3, 1]), 5)
        self.assertEqual(solution.findShortestSubArray([10, 2, 9, 3, 1, 4, 2]), 6)
        self.assertEqual(solution.findShortestSubArray([10, 2, 9, 3, 1, 4, 2]), 6)
        self.assertEqual(solution.findShortestSubArray([1, 1, 1, 1]), 4)
        self.assertEqual(solution.findShortestSubArray([1, 1]), 2)
        self.assertEqual(solution.findShortestSubArray([1, 2, 3, 4]), 1)

if __name__ == '__main__':
    unittest.main()
