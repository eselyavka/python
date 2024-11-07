#!/usr/bin/env python

import unittest


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        seen = [False for _ in range(len(M))]

        def dfs(grid, seen, i):
            seen[i] = True
            for j in range(len(grid)):
                if grid[i][j] and not seen[j]:
                    dfs(grid, seen, j)

        res = 0
        n = len(M)
        for i in range(n):
            if not seen[i]:
                dfs(M, seen, i)
                res += 1

        return res


class TestSolution(unittest.TestCase):

    def test_findCircleNum(self):
        grid = [[1, 1, 0],
                [1, 1, 0],
                [0, 0, 1]]
        grid2 = [[1, 1, 0],
                 [1, 1, 1],
                 [0, 1, 1]]

        solution = Solution()
        self.assertEqual(solution.findCircleNum(grid), 2)
        self.assertEqual(solution.findCircleNum(grid2), 1)


if __name__ == '__main__':
    unittest.main()
