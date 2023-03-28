import unittest
from collections import defaultdict, deque


class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        G = defaultdict(set)

        for gene in [startGene] + bank:
            for item in bank:
                distance = sum([a != b for a, b in zip(gene, item)])
                if distance == 1:
                    G[gene].add(item)

        ans = float("+inf")
        q = deque()
        path = [startGene]
        q.append(path[:])

        while q:
            p = q.popleft()
            last = p[-1]

            if last == endGene:
                ans = min(len(p) - 1, ans)

            for vertex in G[last]:
                if vertex not in p:
                    newpath = p[:]
                    newpath.append(vertex)
                    q.append(newpath)

        return -1 if ans == float("+inf") else ans


class TestSolution(unittest.TestCase):
    def test_minMutation(self):
        solution = Solution()
        self.assertEqual(solution.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]), 2)


if __name__ == '__main__':
    unittest.main()
