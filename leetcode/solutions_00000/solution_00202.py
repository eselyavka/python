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
            n = sum([x ** 2 for x in mas])
            if n == 1:
                return True
            if n in seen:
                return False

            seen.add(n)

            return rec(self.number_to_array(n))

        return rec(self.number_to_array(n))


class Solution2(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def next_num(x):
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d * d
            return s

        slow = n
        fast = next_num(n)

        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))

        return fast == 1


class TestSolution(unittest.TestCase):

    def test_isHappy(self):
        solution = Solution()

        self.assertTrue(solution.isHappy(19))
        self.assertTrue(solution.isHappy(7))
        self.assertFalse(solution.isHappy(5))
        self.assertFalse(solution.isHappy(11))
        self.assertFalse(solution.isHappy(78))

        solution = Solution2()

        self.assertTrue(solution.isHappy(19))
        self.assertTrue(solution.isHappy(7))
        self.assertFalse(solution.isHappy(5))
        self.assertFalse(solution.isHappy(11))
        self.assertFalse(solution.isHappy(78))


if __name__ == '__main__':
    unittest.main()
