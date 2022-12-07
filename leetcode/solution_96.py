import unittest


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 1
        for i in range(1, n + 1):
            res = res * (n + i) / i
        res = res / (n + 1)

        return res


class TestSolution(unittest.TestCase):
    def test_numTrees(self):
        solution = Solution()
        self.assertEqual(solution.numTrees(5), 42)


if __name__ == '__main__':
    unittest.main()
