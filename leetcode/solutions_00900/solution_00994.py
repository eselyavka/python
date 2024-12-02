import unittest
from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def could_be_infected(x, y, grid):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                if grid[x][y] == 1:
                    return True

            return False

        def contaminating_process(ts):
            is_infected = False
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == ts:
                        for dx, dy in dirs:
                            x = i + dx
                            y = j + dy
                            if could_be_infected(x, y, grid):
                                is_infected = True
                                grid[x][y] = ts + 1
            return is_infected

        ts = 2
        while contaminating_process(ts):
            ts += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return ts - 2


class Solution2(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        fresh_oranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh_oranges += 1

        ans = -1
        seen = [[False] * n for _ in range(m)]
        for q in queue:
            seen[q[0]][q[1]] = True

        queue.append((-1, -1))

        while queue:
            cnt = len(queue)
            while cnt > 0:
                x, y = queue.popleft()
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    dx = x + d[0]
                    dy = y + d[1]
                    if 0 <= dx < m and 0 <= dy < n and seen[dx][dy] == False:
                        seen[dx][dy] = True
                        if grid[dx][dy] == 1:
                            grid[dx][dy] = 2
                            queue.append((dx, dy))
                            fresh_oranges -= 1
                cnt -= 1
            ans += 1

        return ans if fresh_oranges == 0 else -1


class TestSolution(unittest.TestCase):
    def test_orangesRotting(self):
        solution = Solution()
        self.assertEqual(solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4)
        solution2 = Solution2()
        self.assertEqual(solution2.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4)


if __name__ == '__main__':
    unittest.main()
