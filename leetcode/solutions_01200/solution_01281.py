#!/usr/bin/env python

import unittest


class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return 0

        product, sum_ = 1, 0

        while n:
            product *= n % 10
            sum_ += n % 10
            n //= 10

        return product - sum_


class TestSolution(unittest.TestCase):
    def test_subtractProductAndSum(self):
        solution = Solution()
        self.assertEqual(solution.subtractProductAndSum(234), 15)


if __name__ == '__main__':
    unittest.main()
