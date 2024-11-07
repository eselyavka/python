#!/usr/bin/env python

import unittest


class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefix_sum = [arr[0]]
        init_var = arr[0]
        for i in range(1, len(arr)):
            prefix_sum.append(init_var ^ arr[i])
            init_var = init_var ^ arr[i]

        res = []

        for q in queries:
            i, j = q
            if not i:
                res.append(prefix_sum[j])
            else:
                res.append(prefix_sum[j] ^ prefix_sum[i-1])

        return res


class TestSolution(unittest.TestCase):
    def test_xorQueries(self):
        solution = Solution()
        self.assertListEqual(solution.xorQueries([1, 3, 4, 8],
                                                 [[0, 1], [1, 2], [0, 3], [3, 3]]),
                             [2, 7, 14, 8])


if __name__ == '__main__':
    unittest.main()
