import unittest


class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m = len(maze)
        n = len(maze[0])

        visited = [[False] * n for _ in range(m)]

        def dfs(maze, pos, destination):

            if visited[pos[0]][pos[1]]:
                return False

            if pos == destination:
                return True

            visited[pos[0]][pos[1]] = True

            r = pos[1] + 1
            l = pos[1] - 1
            u = pos[0] + 1
            d = pos[0] - 1

            # right
            while r < n and maze[pos[0]][r] == 0:
                r += 1
            if dfs(maze, (pos[0], r - 1), destination):
                return True

            # left
            while l >= 0 and maze[pos[0]][l] == 0:
                l -= 1
            if dfs(maze, (pos[0], l + 1), destination):
                return True

            # up
            while u < m and maze[u][pos[1]] == 0:
                u += 1
            if dfs(maze, (u - 1, pos[1]), destination):
                return True

            # down
            while d >= 0 and maze[d][pos[1]] == 0:
                d -= 1
            if dfs(maze, (d + 1, pos[1]), destination):
                return True

            return False

        return dfs(maze, tuple(start), tuple(destination))


class TestCase(unittest.TestCase):
    def test_hasPath(self):
        solution = Solution()
        self.assertTrue(
            solution.hasPath([[0, 0, 1, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 1, 0],
                              [1, 1, 0, 1, 1],
                              [0, 0, 0, 0, 0]],
                             [0, 4], [4, 4]))


if __name__ == '__main__':
    unittest.main()
