#!/usr/bin/env python

import unittest

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if not bills:
            return False

        if bills[0] > 5:
            return False

        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                five -= 1
            elif bill == 20 and ten > 0 and five >= 1:
                ten -= 1
                five -= 1
            elif bill == 20 and five > 3:
                five -= 3
            else:
                return False

        return True


class TestSolution(unittest.TestCase):
    def test_lemonadeChange(self):
        solution = Solution()
        self.assertTrue(solution.lemonadeChange([5, 5, 5, 10, 20]))


if __name__ == '__main__':
    unittest.main()
