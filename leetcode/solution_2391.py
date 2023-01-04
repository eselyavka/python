import unittest


class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        glass_track, metal_track, paper_track = 0, 0, 0

        prefix_travel = [0 for _ in range(len(travel))]
        prefix_travel[0] = travel[0]
        for i in range(1, len(travel)):
            prefix_travel[i] = prefix_travel[i - 1] + travel[i]

        n = len(garbage)

        metal_idx, glass_idx, paper_idx = -1, -1, -1
        for i in range(n):
            paper = garbage[i].count("P")
            glass = garbage[i].count("G")
            metal = garbage[i].count("M")
            if paper:
                paper_track += paper
                paper_idx = i - 1 if i > 0 else -1
            if metal:
                metal_track += metal
                metal_idx = i - 1 if i > 0 else -1
            if glass:
                glass_track += glass
                glass_idx = i - 1 if i > 0 else -1

        ans = (glass_track + (prefix_travel[glass_idx] if glass_idx > -1 else 0)) + (
                metal_track + (prefix_travel[metal_idx] if metal_idx > -1 else 0)) + (
                      paper_track + (prefix_travel[paper_idx] if paper_idx > -1 else 0))

        return ans


class TestSolution(unittest.TestCase):
    def test_garbageCollection(self):
        solution = Solution()
        self.assertEqual(solution.garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]), 21)


if __name__ == '__main__':
    unittest.main()
