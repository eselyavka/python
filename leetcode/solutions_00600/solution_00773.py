#!/usr/bin/env python

import unittest


class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        m = len(board)
        n = len(board[0])

        def find_zero(matrix):
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == 0:
                        return (i, j)

        def valid(board):
            return board[0] == [1, 2, 3] and board[1] == [4, 5, 0]

        if valid(board):
            return 0

        queue = [(0, board)]
        seen = {tuple(tuple(row) for row in board)}

        while queue:
            cnt = len(queue)
            while cnt:
                ans, node = queue.pop(0)
                if valid(node):
                    return ans

                x, y = find_zero(node)

                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    dx = x + d[0]
                    dy = y + d[1]
                    if 0 <= dx < m and 0 <= dy < n:
                        new_node = [row[:] for row in node]
                        new_node[x][y], new_node[dx][dy] = new_node[dx][dy], new_node[x][y]
                        new_node_tuple = tuple(tuple(row) for row in new_node)
                        if new_node_tuple not in seen:
                            seen.add(new_node_tuple)
                            queue.append((ans + 1, new_node))

                cnt -= 1

        return -1


class TestSolution(unittest.TestCase):
    def test_slidingPuzzle(self):
        solution = Solution()
        self.assertEqual(solution.slidingPuzzle([[4, 1, 2], [5, 0, 3]]), 5)
        self.assertEqual(solution.slidingPuzzle([[1, 2, 3], [5, 4, 0]]), -1)


if __name__ == '__main__':
    unittest.main()
