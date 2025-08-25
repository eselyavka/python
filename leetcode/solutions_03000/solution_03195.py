import unittest


class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        x_min, y_min = float("+inf"), float("+inf")
        x_max, y_max = -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x_min = min(x_min, i)
                    y_min = min(y_min, j)
                    x_max = max(x_max, i)
                    y_max = max(y_max, j)

        return abs(x_max - x_min + 1) * abs(y_max - y_min + 1)


class TestSolution(unittest.TestCase):
    def test_minimumArea(self):
        solution = Solution()
        self.assertEqual(solution.minimumArea([[0, 1, 0], [1, 0, 1]]), 6)


if __name__ == '__main__':
    unittest.main()
