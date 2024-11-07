import heapq
import unittest


class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            heapq.heapify(grid[i])

        i, j = 0, 0
        ans = 0
        row_min = []
        while j < m * n:
            if i == m:
                i = 0
                ans += max(row_min)
                row_min = []
            row_min.append(heapq.heappop(grid[i]))
            i += 1
            j += 1

        ans += max(row_min)

        return ans


class TestSolution(unittest.TestCase):
    def test_deleteGreatestValue(self):
        solution = Solution()
        self.assertEqual(solution.deleteGreatestValue([[1, 2, 4], [3, 3, 1]]), 8)


if __name__ == '__main__':
    unittest.main()
