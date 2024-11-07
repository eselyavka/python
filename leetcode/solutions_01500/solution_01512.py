#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(list)
        res = 0
        for idx, num in enumerate(nums):
            if d[num] and d[num][-1] < idx:
                res += len(d[num])

            d[num].append(idx)

        return res


class TestSolution(unittest.TestCase):
    def test_numIdenticalPairs(self):
        solution = Solution()
        self.assertEqual(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]), 4)


if __name__ == '__main__':
    unittest.main()
