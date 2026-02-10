import heapq
from collections import defaultdict

import unittest


class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        G = defaultdict(list)

        for edge in edges:
            u, v, w = edge
            G[u].append([w, v])
            G[v].append([2 * w, u])

        dist = [float("+inf")] * n
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            d, v = heapq.heappop(pq)
            if d > dist[v]:
                continue
            for w, u in G[v]:
                nd = w + d
                if nd < dist[u]:
                    dist[u] = nd
                    heapq.heappush(pq, (nd, u))

        return dist[n - 1] if dist[n - 1] != float("+inf") else -1


class TestSolution(unittest.TestCase):
    def test_minCost(self):
        solution = Solution()
        self.assertEqual(solution.minCost(4, [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]), 5)


if __name__ == '__main__':
    unittest.main()
