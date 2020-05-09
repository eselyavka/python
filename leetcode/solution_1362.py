#!/usr/bin/env python

import unittest


class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def divisors(n):
            divisors = [1, n]
            i = 2
            while i ** 2 <= n:
                if n % i == 0:
                    divisors = [i, n / i]
                i += 1

            return divisors

        div_one = divisors(num + 1)
        div_two = divisors(num + 2)

        return div_one if abs(div_one[0] - div_one[1]) < abs(div_two[0] - div_two[1]) else div_two


class TestSolution(unittest.TestCase):

    def test_closestDivisors(self):
        solution = Solution()
        self.assertEqual(solution.closestDivisors(1), [1, 2])
        self.assertEqual(solution.closestDivisors(8), [3, 3])


if __name__ == '__main__':
    unittest.main()
