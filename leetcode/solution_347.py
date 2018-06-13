#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = defaultdict(int)

        for num in nums:
            d[num] += 1
        res = d.items()
        res.sort(key=lambda x: x[1])
        return [x[0] for x in res[:-(k+1):-1]]


class TestSolution(unittest.TestCase):

    def test_topKFrequent(self):
        solution = Solution()

        arr = [4, 5, 1, 1, 1, 2, 2, 3]

        solution.topKFrequent(arr, 2)

        self.assertEqual(solution.topKFrequent(arr, 2),
                         [1, 2])

if __name__ == '__main__':
    unittest.main()
