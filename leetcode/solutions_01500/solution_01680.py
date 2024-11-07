import unittest


class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        acc = ""
        if n == 0:
            return 0

        if n == 1:
            return 1

        i = 1
        while i <= n:
            acc += bin(i)[2:]
            i += 1

        return int(acc, 2) % (pow(10, 9) + 7)


class TestSolution(unittest.TestCase):
    def test_concatenatedBinary(self):
        solution = Solution()
        self.assertEqual(solution.concatenatedBinary(3), 27)


if __name__ == '__main__':
    unittest.main()
