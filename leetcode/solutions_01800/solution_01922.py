import unittest


class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod_ = 10 ** 9 + 7

        def binpow(x, y):
            if y == 0:
                return 1

            res = binpow(x, y // 2)

            if y % 2:
                return (res * res * x) % mod_

            return (res * res) % mod_

        return (binpow(5, (n + 1) // 2) * binpow(4, n // 2)) % mod_


class TestSolution(unittest.TestCase):
    def test_countGoodNumbers(self):
        solution = Solution()
        self.assertEqual(solution.countGoodNumbers(4), 400)


if __name__ == '__main__':
    unittest.main()
