import heapq
import unittest


class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])
        h = []

        def rhombus(grid, l, r, u, d):
            c1 = c2 = (l + r) // 2
            ssum = 0
            expand = True
            for idx in range(u, d + 1):
                if c1 == c2:
                    ssum += grid[idx][c1]
                else:
                    ssum += grid[idx][c1] + grid[idx][c2]

                if c1 == l:
                    expand = False

                if expand:
                    c1 -= 1
                    c2 += 1
                else:
                    c1 += 1
                    c2 -= 1

            return ssum

        for i in range(m):
            for j in range(n):
                l = r = j
                d = i
                while l >= 0 and r < n and d < m:
                    ssum = rhombus(grid, l, r, i, d)
                    heapq.heappush(h, -ssum)
                    l -= 1
                    r += 1
                    d += 2

        ans = []
        while h:
            val = heapq.heappop(h)
            if not ans or ans[-1] != -val:
                ans.append(-val)
            if len(ans) == 3:
                break

        return ans


class TestSolution(unittest.TestCase):
    def test_getBiggestThree(self):
        solution = Solution()
        self.assertListEqual(solution.getBiggestThree(
            [[3, 4, 5, 1, 3],
             [3, 3, 4, 2, 3],
             [20, 30, 200, 40, 10],
             [1, 5, 5, 4, 1],
             [4, 3, 2, 2, 5]]),
                             [228, 216, 211])


if __name__ == '__main__':
    unittest.main()
