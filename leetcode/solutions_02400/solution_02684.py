import unittest

from collections import deque


class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        visited = [[False for x in range(n)] for y in range(m)]
        moves = 0
        q = deque()
        for i in range(m):
            q.append((i, 0, 0))

        while q:
            length = len(q)
            for _ in range(length):
                x, y, cnt = q.popleft()
                moves = max(moves, cnt)
                for d in [(-1, 1), (0, 1), (1, 1)]:
                    dx = x + d[0]
                    dy = y + d[1]
                    if 0 <= dx < m and 0 <= dy < n and not visited[dx][dy] and grid[dx][dy] > grid[x][y]:
                        visited[dx][dy] = True
                        q.append((dx, dy, cnt + 1))
        return moves


class TestSolution(unittest.TestCase):
    def test_maxMoves(self):
        solution = Solution()
        self.assertEqual(solution.maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]), 3)
        self.assertEqual(solution.maxMoves([[3, 2, 4], [2, 1, 9], [1, 1, 7]]), 0)


if __name__ == '__main__':
    unittest.main()
