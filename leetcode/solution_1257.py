import unittest


class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """

        root = regions[0][0]
        G = {}

        for region in regions:
            G[region[0]] = region[1:]

        paths = {}

        def dfs(root, G, path, r):
            if root not in G:
                return

            path.append(root)

            if r in G[root]:
                paths[r] = path[:] + [r]
                return

            for item in G[root]:
                dfs(item, G, path, r)

            path.pop()

        dfs(root, G, [], region1)
        dfs(root, G, [], region2)

        arr1 = paths[region1]
        arr2 = paths[region2]
        n = min(len(arr1), len(arr2))

        prev = arr1[0]

        for i in range(n):
            if arr1[i] != arr2[i]:
                return prev
            prev = arr1[i]

        return prev


class TestSolution(unittest.TestCase):
    def test_findSmallestRegion(self):
        solution = Solution()
        self.assertEqual(solution.findSmallestRegion([["Earth", "North America", "South America"],
                                                      ["North America", "United States", "Canada"],
                                                      ["United States", "New York", "Boston"],
                                                      ["Canada", "Ontario", "Quebec"],
                                                      ["South America", "Brazil"]],
                                                     "Quebec", "New York"),
                         "North America")


if __name__ == '__main__':
    unittest.main()
