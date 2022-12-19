import unittest
from collections import defaultdict


class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        if len(bombs) == 1:
            return 1

        G = defaultdict(list)
        n = len(bombs)

        for i in range(n):
            x1, y1, r1 = bombs[i]
            G[i].append(i)
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                if r1 >= d:
                    G[i].append(j)

        def dfs(visited, graph, node):
            if not node in visited:
                visited.add(node)
                for neighbour in graph[node]:
                    dfs(visited, graph, neighbour)

        ans = 1
        for i in range(n):
            visited = set()
            dfs(visited, G, i)
            ans = max(ans, len(visited))

        return ans


class TestSolution(unittest.TestCase):
    def test_maximumDetonation(self):
        solution = Solution()
        self.assertEqual(solution.maximumDetonation([[2, 1, 3], [6, 1, 4]]), 2)


if __name__ == '__main__':
    unittest.main()
