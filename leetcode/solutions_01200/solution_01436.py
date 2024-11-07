import unittest


class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        G = {}

        for start, end in paths:
            G[start] = end

        ans = paths[0][0]

        while True:
            if ans in G:
                ans = G[ans]
                continue
            return ans


class TestSolution(unittest.TestCase):
    def test_destCity(self):
        solution = Solution()
        self.assertEqual(solution.destCity([["London", "New York"],
                                            ["New York", "Lima"],
                                            ["Lima", "Sao Paulo"]]),
                         "Sao Paulo")


if __name__ == '__main__':
    unittest.main()
