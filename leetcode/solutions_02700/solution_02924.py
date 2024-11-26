import unittest


class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        arr = [0] * n

        for _, weaker in edges:
            arr[weaker] += 1

        champ = -1
        champ_count = 0

        for i in range(n):
            if arr[i] == 0:
                champ_count += 1
                champ = i

        return champ if champ_count == 1 else -1


class TestSolution(unittest.TestCase):
    def test_findChampion(self):
        solution = Solution()
        self.assertEqual(solution.findChampion(3, [[0, 1], [1, 2]]), 0)


if __name__ == '__main__':
    unittest.main()
