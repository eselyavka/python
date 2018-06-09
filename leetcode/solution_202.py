#!/usr/bin/env python

import unittest

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = set()

        def rec(n):
            def num_to_array(num, base):
                if num < base:
                    return [num]
                return num_to_array(num // base, base) + [num%base]

            num = sum([x**2 for x in num_to_array(n, 10)])

            if num == 1:
                return True
            elif num in d:
                return False
            else:
                d.add(num)

            return rec(num)

        return rec(n)

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
