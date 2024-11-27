import unittest

from collections import deque, defaultdict


class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        def bfs(graph, n):
            visited = [False] * n
            queue = deque()
            queue.append(0)
            visited[0] = True

            path = 0
            while queue:
                cnt = len(queue)
                while cnt > 0:
                    node = queue.popleft()
                    if node == n - 1:
                        return path
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor] = True
                    cnt -= 1
                path += 1

            return -1

        G = defaultdict(list)
        for i in range(1, n):
            G[i - 1].append(i)

        ans = []
        for u, v in queries:
            G[u].append(v)
            ans.append(bfs(G, n))

        return ans


class TestSolution(unittest.TestCase):
    def test_compressedString(self):
        solution = Solution()
        self.assertEqual(solution.shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]]), [3, 2, 1])


if __name__ == '__main__':
    unittest.main()
