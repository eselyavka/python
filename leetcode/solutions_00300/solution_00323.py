import unittest
from collections import defaultdict


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        G = defaultdict(list)

        for a, b in edges:
            G[a].append(b)
            G[b].append(a)

        ans = 0
        visited = {k: False for k in range(n)}

        def dfs(V, k, visited):
            visited[k] = True
            for neighbor in V:
                if not visited[neighbor]:
                    dfs(G[neighbor], neighbor, visited)

        for k in range(n):
            if not visited[k]:
                dfs(G[k], k, visited)
                ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_countComponents(self):
        solution = Solution()
        self.assertEqual(solution.countComponents(5, [[0, 1], [1, 2], [3, 4]]), 2)


if __name__ == '__main__':
    unittest.main()
