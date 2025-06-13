import unittest


class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        ps = 0
        max_ps = 0
        min_ps = 0

        for d in differences:
            ps += d
            max_ps = max(ps, max_ps)
            min_ps = min(ps, min_ps)

        low = lower - min_ps
        hi = upper - max_ps

        return max(0, hi - low + 1)


class TestSolution(unittest.TestCase):
    def test_numberOfArrays(self):
        solution = Solution()
        self.assertEqual(solution.numberOfArrays([1, -3, 4], 1, 6), 2)


if __name__ == '__main__':
    unittest.main()
