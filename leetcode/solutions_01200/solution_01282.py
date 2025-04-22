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


class Solution2(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """

        buckets = defaultdict(list)

        for idx, gr_id in enumerate(groupSizes):
            buckets[gr_id].append(idx)

        ans = []
        for gr_id in buckets:
            lst = buckets[gr_id]
            ans.extend(lst[i:i + gr_id] for i in range(0, len(lst), gr_id))

        return ans


class TestSolution(unittest.TestCase):

    def arrays_equal(self, a, b):
        if len(a) != len(b):
            return False
        for row1, row2 in zip(a, b):
            if len(row1) != len(row2):
                return False
            for x, y in zip(row1, row2):
                if x != y:
                    return False
        return True

    def test_groupThePeople(self):
        solution = Solution()
        self.assertTrue(self.arrays_equal(solution.groupThePeople([3, 3, 3, 3, 3, 1, 3]),
                                          [[0, 1, 2], [3, 4, 6], [5]]))
        solution = Solution2()
        self.assertTrue(self.arrays_equal(solution.groupThePeople([3, 3, 3, 3, 3, 1, 3]),
                                          [[0, 1, 2], [3, 4, 6], [5]]))


if __name__ == '__main__':
    unittest.main()
