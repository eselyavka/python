#!/usr/bin/env python

import unittest


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0] * n for _ in range(n)]

        i = 2

        prev_x = 0
        prev_y = 0
        ans[prev_x][prev_y] = 1

        while i <= n ** 2:
            # right
            while True:
                new_x = min(prev_x, n - 1)
                new_y = min(prev_y + 1, n - 1)
                if ans[new_x][new_y] == 0:
                    ans[new_x][new_y] = i
                    i += 1
                    prev_x, prev_y = new_x, new_y
                else:
                    break
            # down
            while True:
                new_x = min(prev_x + 1, n - 1)
                new_y = min(prev_y, n - 1)
                if ans[new_x][new_y] == 0:
                    ans[new_x][new_y] = i
                    i += 1
                    prev_x, prev_y = new_x, new_y
                else:
                    break
                    # left
            while True:
                new_x = min(prev_x, n - 1)
                new_y = min(prev_y - 1, n - 1)
                if ans[new_x][new_y] == 0:
                    ans[new_x][new_y] = i
                    i += 1
                    prev_x, prev_y = new_x, new_y
                else:
                    break
            # up
            while True:
                new_x = min(prev_x - 1, n - 1)
                new_y = min(prev_y, n - 1)
                if ans[new_x][new_y] == 0:
                    ans[new_x][new_y] = i
                    i += 1
                    prev_x, prev_y = new_x, new_y
                else:
                    break
        return ans


class TestSolution(unittest.TestCase):
    def test_generateMatrix(self):
        solution = Solution()
        self.assertListEqual(solution.generateMatrix(3), [[1, 2, 3],
                                                          [8, 9, 4],
                                                          [7, 6, 5]])


if __name__ == '__main__':
    unittest.main()
