#!/usr/bin/env python

import unittest
from collections import defaultdict


class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        res = []
        buckets = defaultdict(list)

        for i, size in enumerate(groupSizes):
            group = buckets[size]
            if len(group) >= size:
                buckets[size] = [i]
                res.append(group)
            else:
                buckets[size].append(i)

        res.extend(buckets.values())

        return res


class TestSolution(unittest.TestCase):

    def test_groupThePeople(self):
        solution = Solution()
        self.assertListEqual(solution.groupThePeople([3, 3, 3, 3, 3, 1, 3]),
                             [[0, 1, 2], [5], [3, 4, 6]])


if __name__ == '__main__':
    unittest.main()
