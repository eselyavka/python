import unittest


class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        while True:
            if n & (n + 1) == 0:
                return n
            n += 1


class TestSolution(unittest.TestCase):
    def test_smallestNumber(self):
        solution = Solution()
        self.assertEqual(solution.smallestNumber(5), 7)


if __name__ == '__main__':
    unittest.main()
