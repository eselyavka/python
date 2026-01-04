import unittest


class Solution(object):
    def getDescentPeriods(self, prices):
        n = len(prices)
        ans = 0
        run = 0

        for i in range(n):
            if i > 0 and prices[i - 1] - prices[i] == 1:
                run += 1
            else:
                run = 1

            ans += run

        return ans


class TestSolution(unittest.TestCase):
    def test_getDescentPeriods(self):
        solution = Solution()
        self.assertEqual(solution.getDescentPeriods([3, 2, 1, 4]), 7)


if __name__ == '__main__':
    unittest.main()
