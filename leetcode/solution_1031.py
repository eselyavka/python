#!/usr/bin/python

import unittest


class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """

        prefix_sum_m = [0] * len(A)
        prefix_sum_l = [0] * len(A)

        for i in range(len(A)):
            if i <= len(A) - M:
                for j in range(i, i+M):
                    prefix_sum_m[i] += A[j]
            if i <= len(A) - L:
                for j in range(i, i+L):
                    prefix_sum_l[i] += A[j]

        max_left_to_right = 0
        i = L
        for num in prefix_sum_l:
            for j in range(i, len(A)):
                max_left_to_right = max(max_left_to_right, num + prefix_sum_m[j])
            i = i + 1

        max_right_to_left = 0
        i = M
        for num in prefix_sum_m:
            for j in range(i, len(A)):
                max_right_to_left = max(max_right_to_left, num + prefix_sum_l[j])
            i = i + 1

        return max(max_left_to_right, max_right_to_left)


class TestSolution(unittest.TestCase):

    def test_maxSumTwoNoOverlap(self):
        solution = Solution()
        self.assertEqual(solution.maxSumTwoNoOverlap(
            [4, 5, 14, 16, 16, 20, 7, 13, 8, 15], 3, 5), 109)
        self.assertEqual(solution.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2), 20)
        self.assertEqual(solution.maxSumTwoNoOverlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2), 29)
        self.assertEqual(solution.maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3), 31)
        self.assertEqual(solution.maxSumTwoNoOverlap([1, 0, 3], 1, 2), 4)


if __name__ == '__main__':
    unittest.main()
