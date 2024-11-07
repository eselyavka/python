#!/usr/bin/env python

import unittest
from collections import defaultdict


class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        row = len(heights)
        col = len(heights[0])

        dst = (row - 1, col - 1)
        adj = [(-1,0), (1,0),(0, -1), (0, 1)]

        def bfs(mid):
            visited = defaultdict(lambda: False)
            visited[(0,0)] = True
            queue = [(0,0)]
            while queue:
                node = queue.pop(0)

                if node == dst:
                    return True

                x, y = node
                visited[(x, y)] = True

                for dx, dy in adj:
                    new_x = dx + x
                    new_y = dy + y

                    if not 0<=new_x<row or not 0<=new_y<col or visited[(new_x,new_y)]:
                        continue

                    curr_diff = abs(heights[new_x][new_y] - heights[x][y])

                    if curr_diff <= mid:
                        visited[(new_x,new_y)] = True
                        queue.append((new_x, new_y))

        left = 0
        right = 10000000
        while left < right:
            mid = (left + right) // 2
            if bfs(mid):
                right = mid
            else:
                left = mid + 1

        return left


class TestSolution(unittest.TestCase):

    def test_minimumEffortPath(self):
        solution = Solution()

        self.assertEqual(solution.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]), 2)


if __name__ == '__main__':
    unittest.main()
