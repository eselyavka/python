#!/usr/bin/env python3

"""LeetCode solution 01536."""

import unittest


class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        trailing_zeros = [0] * n

        for i in range(n):
            tail_zeros = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    break
                tail_zeros += 1

            trailing_zeros[i] = tail_zeros

        answer = 0
        for i in range(n - 1):
            required = n - i - 1

            index = -1
            for j in range(i, n):
                if trailing_zeros[j] >= required:
                    index = j
                    break

            if index == -1:
                return -1

            while index > i:
                answer += 1
                trailing_zeros[index - 1], trailing_zeros[index] = (
                    trailing_zeros[index],
                    trailing_zeros[index - 1],
                )
                index -= 1

        return answer


class TestSolution(unittest.TestCase):
    def test_minSwaps(self):
        solution = Solution()
        self.assertEqual(solution.minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]), 3)


if __name__ == '__main__':
    unittest.main()
