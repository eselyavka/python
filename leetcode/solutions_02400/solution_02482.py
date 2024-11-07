import unittest


class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])

        d_row = {}
        d_col = {}

        # row traversal
        for i in range(m):
            onesRow = sum(grid[i])
            zerosRow = n - onesRow
            d_row[i] = (onesRow, zerosRow)

        # column traversal
        for j in range(n):
            onesCol = 0
            for i in range(m):
                onesCol += grid[i][j]
            zerosCol = m - onesCol
            d_col[j] = (onesCol, zerosCol)

        ans = [[None] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = d_row[i][0] + d_col[j][0] - d_row[i][1] - d_col[j][1]

        return ans


class TestSolution(unittest.TestCase):
    def test_onesMinusZeros(self):
        solution = Solution()
        self.assertEqual(solution.onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]),
                         [[0, 0, 4], [0, 0, 4], [-2, -2, 2]])


if __name__ == '__main__':
    unittest.main()
