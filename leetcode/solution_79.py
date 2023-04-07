import unittest


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        path = []

        def dfs(x, y, pos):
            if pos == len(word):
                return True

            if 0 <= x < m and 0 <= y < n and board[x][y] == word[pos] and (x, y) not in path:
                path.append((x, y))

                res = dfs(x + 1, y, pos + 1) or dfs(x - 1, y, pos + 1) or dfs(x, y + 1, pos + 1) or dfs(x, y - 1,
                                                                                                        pos + 1)

                path.pop()

                return res

            return False

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True

        return False


class TestSolution(unittest.TestCase):
    def test_exist(self):
        solution = Solution()
        self.assertTrue(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))


if __name__ == '__main__':
    unittest.main()
