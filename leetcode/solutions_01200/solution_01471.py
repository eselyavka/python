#!/usr/bin/env python

import unittest


class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(arr) == 1:
            return arr

        m = sorted(arr)[(len(arr) - 1)/2]

        t_arr = [tuple([x, abs(x-m)]) for x in arr]

        def cmp_(x, y):
            if x[1] > y[1]:
                return 1
            elif x[1] < y[1]:
                return -1
            else:
                if x[0] > y[0]:
                    return 1
                elif x[0] < y[0]:
                    return -1
                return 0

        res = sorted(t_arr, cmp=cmp_)

        return [x[0] for x in res[-k:]]


class TestSolution(unittest.TestCase):

    def test_getStrongest(self):
        solution = Solution()
        self.assertListEqual(solution.getStrongest(
            [-2, -4, -6, -8, -9, -7, -5, -3, -1], 2),
                             [-2, -9, -1])


if __name__ == '__main__':
    unittest.main()
