import unittest


class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        arr = [0] * m

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    arr[row] += 1

        champ = -1
        champ_idx = -1
        for i in range(m):
            if arr[i] > champ:
                champ = arr[i]
                champ_idx = i

        return champ_idx


class TestSolution(unittest.TestCase):
    def test_findChampion(self):
        solution = Solution()
        self.assertEqual(solution.findChampion([[0, 0, 1], [1, 0, 1], [0, 0, 0]]), 1)


if __name__ == '__main__':
    unittest.main()
