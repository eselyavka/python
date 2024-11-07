#!/usr/bin/env python

import unittest


class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        memo = [[float('+inf') for _ in range(m)] for _ in range(n)]
        q = [(0, 0, 0, 0)]  # x, y, steps and obstacles

        while q:
            size = len(q)
            while size:
                size -= 1

                x, y, steps, obs = q.pop(0)

                if obs > k:
                    continue

                if x == n - 1 and y == m - 1:
                    return steps

                for r, c in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
                    if 0 <= r < n and 0 <= c < m:
                        obs_ = obs+1 if grid[r][c] else obs
                        if memo[r][c] > obs_:
                            memo[r][c] = obs_
                            q.append((r, c, steps + 1, obs_))
        return -1


class TestSolution(unittest.TestCase):
    def test_shortestPath(self):
        solution = Solution()
        self.assertEqual(solution.shortestPath([[0, 1, 1],
                                                [1, 1, 1],
                                                [1, 0, 0]], 1), -1)


if __name__ == '__main__':
    unittest.main()
