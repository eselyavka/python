import unittest


class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0] * 10001
        ans[1] = 1
        ans[2] = 2
        ans[3] = 5

        for i in range(4, n + 1):
            ans[i] = 2 * ans[i - 1] + ans[i - 3]

        return ans[n] % 1000000007


class TestSolution(unittest.TestCase):
    def test_numTilings(self):
        solution = Solution()
        self.assertEqual(solution.numTilings(4), 11)


if __name__ == '__main__':
    unittest.main()
