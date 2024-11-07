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

    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if digits[-1] + 1 < 10:
            digits[-1] += 1
            return digits
        else:
            pivotal = None
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] + 1 < 10:
                    pivotal = i
                    break

            if pivotal is None:
                return [1] + [0] * len(digits)

            digits[pivotal] = digits[pivotal] + 1
            digits = digits[:pivotal+1] + [0] * (len(digits) - (pivotal + 1))

            return digits


class TestSolution(unittest.TestCase):
    def test_plusOne(self):
        solution = Solution()
        self.assertListEqual(solution.plusOne([0]), [1])
        self.assertListEqual(solution.plusOne([1]), [2])
        self.assertListEqual(solution.plusOne([1, 2, 3]), [1, 2, 4])
        self.assertListEqual(solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
        self.assertListEqual(solution.plusOne([9, 9]), [1, 0, 0])
        self.assertListEqual(solution.plusOne([9, 9, 9]), [1, 0, 0, 0])

    def test_plusOne2(self):
        solution = Solution()
        self.assertListEqual(solution.plusOne2([9]), [1, 0])
        self.assertListEqual(solution.plusOne2([9, 9]), [1, 0, 0])
        self.assertListEqual(solution.plusOne2([3, 9, 9]), [4, 0, 0])
        self.assertListEqual(solution.plusOne2([4, 3, 9, 9]), [4, 4, 0, 0])
        self.assertListEqual(solution.plusOne2([0]), [1])
        self.assertListEqual(solution.plusOne2([1]), [2])
        self.assertListEqual(solution.plusOne2([1, 2, 3]), [1, 2, 4])
        self.assertListEqual(solution.plusOne2([4, 3, 2, 1]), [4, 3, 2, 2])


if __name__ == '__main__':
    unittest.main()
