#!/usr/bin/env python

import unittest


class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        def reverse(end):
            start = 0
            while start < end:
                tmp = A[start]
                A[start] = A[end]
                A[end] = tmp
                start += 1
                end -= 1

        res = []
        i = len(A)
        while i > 1:
            idx = A.index(i)
            if idx != i - 1:
                reverse(idx)
                res.append(idx + 1)
                reverse(i-1)
                res.append(i)
            i -= 1

        return res


class TestSolution(unittest.TestCase):

    def test_pancakeSort(self):
        solution = Solution()
        self.assertListEqual(solution.pancakeSort([3, 2, 4, 1]), [3, 4, 2, 3, 1, 2])


if __name__ == '__main__':
    unittest.main()
