import unittest


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (-1, -1), (1, -1)]

        def is_live(x, y, board):
            if 0 <= x < m and 0 <= y < n:
                if board[x][y] == 1:
                    return 1

            return 0

        changes = []

        for i in range(m):
            for j in range(n):
                live = 0
                for dir_ in dirs:
                    dx, dy = dir_
                    newx = i + dx
                    newy = j + dy

                    live += is_live(newx, newy, board)

                if live < 2:
                    changes.append((i, j, 0))

                if live > 3:
                    changes.append((i, j, 0))

                if live == 3 and board[i][j] == 0:
                    changes.append((i, j, 1))

        for change in changes:
            x, y, val = change
            board[x][y] = val


class TestSolution(unittest.TestCase):
    def test_gameOfLife(self):
        solution = Solution()
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        solution.gameOfLife(board)
        self.assertListEqual(board, [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])


if __name__ == '__main__':
    unittest.main()
