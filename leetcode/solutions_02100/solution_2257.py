#!/usr/bin/env python

import unittest


class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[""] * n for _ in range(m)]

        for x, y in walls:
            grid[x][y] = "W"

        for x, y in guards:
            grid[x][y] = "G"

        seen = set()
        for x, y in guards:
            dx = x + 1
            while dx < m and grid[dx][y] == "":
                seen.add((dx, y))
                dx += 1
            dx = x - 1
            while dx >= 0 and grid[dx][y] == "":
                seen.add((dx, y))
                dx -= 1
            dy = y + 1
            while dy < n and grid[x][dy] == "":
                seen.add((x, dy))
                dy += 1
            dy = y - 1
            while dy >= 0 and grid[x][dy] == "":
                seen.add((x, dy))
                dy -= 1

        return (m * n) - len(guards) - len(walls) - len(seen)


class TestSolution(unittest.TestCase):
    def test_countUnguarded(self):
        solution = Solution()
        self.assertEqual(solution.countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]), 7)


if __name__ == '__main__':
    unittest.main()
