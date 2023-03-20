import unittest


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


class TestSolution(unittest.TestCase):
    def test_orangesRotting(self):
        solution = Solution()
        self.assertEqual(solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4)


if __name__ == '__main__':
    unittest.main()
