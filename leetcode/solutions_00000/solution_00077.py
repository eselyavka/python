#!/usr/bin/env python

import unittest


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = list()

        def perebor(arr, data, s, e, idx, r):
            if idx == r:
                res.append(data[:])
                return

            i = s
            while i <= e and e - i + 1 >= r - idx:
                data[idx] = arr[i]
                perebor(arr, data, i + 1, e, idx + 1, r)
                i += 1

        arr = range(1, n+1)
        data = [0] * k

        perebor(arr, data, 0, n - 1, 0, k)

        return res


class TestSolution(unittest.TestCase):

    def test_combine(self):
        solution = Solution()
        self.assertListEqual(solution.combine(4, 2), [[1, 2],
                                                      [1, 3],
                                                      [1, 4],
                                                      [2, 3],
                                                      [2, 4],
                                                      [3, 4]])


if __name__ == '__main__':
    unittest.main()
