#!/usr/bin/env python

import unittest

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        if len(costs) == 1:
            return min(costs[0])

        N = len(costs)
        M = len(costs[0])

        for i in range(1, N):
            for j in range(M):
                if j > 0 and j < M - 1:
                    costs[i][j] += min(costs[i-1][j-1], costs[i-1][j+1])
                elif j == 0:
                    costs[i][j] += min(costs[i-1][j+1], costs[i-1][j+2])
                elif j == M-1:
                    costs[i][j] += min(costs[i-1][j-1], costs[i-1][j-2])

        return min(costs[N-1])

class TestSolution(unittest.TestCase):

    def test_minCost(self):
        solution = Solution()
        self.assertEqual(solution.minCost([[17, 2, 17]]), 2)
        self.assertEqual(solution.minCost([[17, 2, 17],
                                           [15, 300, 1]]), 3)
        self.assertEqual(solution.minCost([[17, 2, 17],
                                           [16, 16, 5],
                                           [14, 3, 19]]), 10)
        self.assertEqual(solution.minCost([[5, 8, 6],
                                           [19, 14, 13],
                                           [7, 5, 12],
                                           [14, 15, 17],
                                           [3, 20, 10]]), 43)
        self.assertEqual(solution.minCost([[17, 19, 16],
                                           [11, 17, 17],
                                           [14, 18, 10],
                                           [17, 20, 17],
                                           [14, 2, 13],
                                           [9, 6, 14],
                                           [20, 5, 17],
                                           [19, 19, 5],
                                           [5, 14, 6],
                                           [9, 17, 19],
                                           [17, 13, 6],
                                           [7, 10, 7],
                                           [2, 18, 15],
                                           [9, 9, 13],
                                           [8, 17, 14],
                                           [8, 20, 11],
                                           [2, 11, 18],
                                           [14, 20, 6],
                                           [10, 1, 9],
                                           [16, 12, 7]]), 159)

if __name__ == '__main__':
    unittest.main()
