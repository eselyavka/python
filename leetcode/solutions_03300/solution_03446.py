import unittest
from collections import defaultdict, deque


class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        diags = defaultdict(list)

        for i in range(n):
            for j in range(n):
                diags[i - j].append(grid[i][j])

        for key, vals in diags.items():
            vals.sort(reverse=(key >= 0))
            diags[key] = deque(vals)

        for i in range(n):
            for j in range(n):
                grid[i][j] = diags[i - j].popleft()

        return grid


class TestSolution(unittest.TestCase):
    def test_sortMatrix(self):
        solution = Solution()
        self.assertEqual(solution.sortMatrix([[1, 7, 3], [9, 8, 2], [4, 5, 6]]), [[8, 2, 3], [9, 6, 7], [4, 5, 1]])


if __name__ == '__main__':
    unittest.main()
