import unittest


class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ans = numBottles
        while numBottles >= numExchange:
            ans += numBottles // numExchange
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)

        return ans


class TestSolution(unittest.TestCase):
    def test_numWaterBottles(self):
        solution = Solution()
        self.assertEqual(solution.numWaterBottles(15, 4), 19)


if __name__ == '__main__':
    unittest.main()
