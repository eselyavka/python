#!/usr/bin/env python

import unittest


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dec = [1,
               4,
               5,
               9,
               10,
               40,
               50,
               90,
               100,
               400,
               500,
               900,
               1000]
        roman = ['I',
                 'IV',
                 'V',
                 'IX',
                 'X',
                 'XL',
                 'L',
                 'XC',
                 'C',
                 'CD',
                 'D',
                 'CM',
                 'M']

        res = []
        i = 12
        while num:
            div = num / dec[i]
            num = num % dec[i]

            while div:
                res.append(roman[i])
                div -= 1

            i -= 1

        return ''.join(res)


class TestSolution(unittest.TestCase):
    def test_intToRoman(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(3), 'III')
        self.assertEqual(solution.intToRoman(4), 'IV')
        self.assertEqual(solution.intToRoman(9), 'IX')
        self.assertEqual(solution.intToRoman(58), 'LVIII')
        self.assertEqual(solution.intToRoman(1994), 'MCMXCIV')


if __name__ == '__main__':
    unittest.main()
