#!/usr/bin/env python

import unittest

class Solution(object):
    def is_power_two(self, num, power=0):
        """
        :type num: int
        :rtype: boolean
        """

        if 1 << power > num:
            return False

        if 1 << power == num:
            return True

        return self.is_power_two(num, power=power+1)

class TestSolution(unittest.TestCase):

    def test_is_power_two(self):
        solution = Solution()
        self.assertFalse(solution.is_power_two(1023))
        self.assertFalse(solution.is_power_two(23))
        self.assertTrue(solution.is_power_two(8))
        self.assertTrue(solution.is_power_two(512))

if __name__ == '__main__':
    unittest.main()
