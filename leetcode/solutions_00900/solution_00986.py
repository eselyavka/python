#!/usr/bin/env python

import unittest


class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []

        for i1 in A:
            s1, e1 = i1
            for i2 in B:
                s2, e2 = i2
                if e1 < s2 or s1 > e2:
                    continue
                res.append([max(s1, s2), min(e1, e2)])

        return res


class TestSolution(unittest.TestCase):

    def test_intervalIntersection(self):
        solution = Solution()
        self.assertListEqual(solution.intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]],
                                                           [[1, 5], [8, 12], [15, 24], [25, 26]]),
                             [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]])


if __name__ == '__main__':
    unittest.main()
