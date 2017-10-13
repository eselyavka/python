#!/usr/bin/env python

import unittest

class Solution(object):
    def myAtoi(self, s):
        """
        :type str: s
        :rtype: int
        """

        s = s.strip()

        if not s:
            return 0

        data = list()
        cond = s[0] in ['-', '+']

        mult = 1

        if cond:
            mult = -1 if s[0] == '-' else 1

        for letter in s[1:] if cond else s:
            try:
                data.append(str(int(letter)))
            except ValueError:
                break

        if not data:
            return 0

        num = mult * int(''.join(data))
        if num > 2147483647:
            _int = 2147483647
        elif num < -2147483648:
            _int = -2147483648
        else:
            _int = num

        return _int

class TestSolution(unittest.TestCase):

    def test_groupAnagrams(self):
        digits = ["", "  -0012a42", "+", "-", "2147483648", "-2147483648"]
        solution = Solution()
        self.assertEqual(solution.myAtoi(digits[0]), 0)
        self.assertEqual(solution.myAtoi(digits[1]), -12)
        self.assertEqual(solution.myAtoi(digits[2]), 0)
        self.assertEqual(solution.myAtoi(digits[3]), 0)
        self.assertEqual(solution.myAtoi(digits[4]), 2147483647)
        self.assertEqual(solution.myAtoi(digits[5]), -2147483647)

if __name__ == '__main__':
    unittest.main()
