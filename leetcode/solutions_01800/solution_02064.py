import math
import unittest


class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """

        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            target = sum([math.ceil(x / float(mid)) for x in quantities])
            if target > n:
                left = mid + 1
            else:
                right = mid
        return left


class TestSolution(unittest.TestCase):
    def test_minimizedMaximum(self):
        solution = Solution()
        self.assertEqual(solution.minimizedMaximum(6, [11, 6]), 3)


if __name__ == '__main__':
    unittest.main()
