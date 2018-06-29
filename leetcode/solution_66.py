#!/usr/bin/env python

import unittest

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        size = len(digits) - 1

        def rec(i=size, digit=0):
            if i < 0:
                if digit > 0:
                    digits.insert(0, digit)
                return

            _plus_one = digits[i] + 1

            if _plus_one < 10:
                digits[i] = _plus_one
            else:
                digits[i] = _plus_one % 10
                rec(i-1, _plus_one // 10)

        rec()

        return digits

class TestSolution(unittest.TestCase):
    def test_plusOne(self):
        solution = Solution()
        self.assertEquals(solution.plusOne([0]), [1])
        self.assertEquals(solution.plusOne([1]), [2])
        self.assertEquals(solution.plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEquals(solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
        self.assertEquals(solution.plusOne([9, 9]), [1, 0, 0])
        self.assertEquals(solution.plusOne([9, 9, 9]), [1, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()
