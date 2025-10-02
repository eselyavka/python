import math
import unittest


class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        E0 = numBottles
        x = numExchange
        if E0 <= 0:
            return 0

        D = (2 * x - 3) ** 2 + 8 * (E0 - 1)

        s = math.sqrt(D)
        t = (-(2 * x - 3) + s) // 2
        if t < 0:
            t = 0

        return int(numBottles + t)


class TestSolution(unittest.TestCase):
    def test_maxBottlesDrunk(self):
        solution = Solution()
        self.assertEqual(solution.maxBottlesDrunk(13, 6), 15)


if __name__ == '__main__':
    unittest.main()
