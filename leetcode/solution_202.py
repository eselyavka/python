#!/usr/bin/env python

import unittest


class Solution(object):
    def number_to_array(self, n):
        if n < 10:
            return [n]

        nums = []
        while n:
            nums.append(n % 10)
            n = n // 10

        return nums

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set([n])

        def rec(mas):
            n = sum([x**2 for x in mas])
            if n == 1:
                return True
            if n in seen:
                return False

            seen.add(n)

            return rec(self.number_to_array(n))

        return rec(self.number_to_array(n))


class TestSolution(unittest.TestCase):

    def test_isHappy(self):
        solution = Solution()

        self.assertTrue(solution.isHappy(19))
        self.assertTrue(solution.isHappy(7))
        self.assertFalse(solution.isHappy(5))
        self.assertFalse(solution.isHappy(11))
        self.assertFalse(solution.isHappy(78))


if __name__ == '__main__':
    unittest.main()
