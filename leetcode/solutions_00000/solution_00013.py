#!/usr/bin/env python

import unittest

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        roman_mapping = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
                         'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
                         'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        i = 0
        while i < len(s):
            n = (s[i] + s[i+1]) if i < len(s) - 1 else None
            if n and roman_mapping.has_key(n):
                res += roman_mapping[n]
                i += 2
            else:
                res += roman_mapping[s[i]]
                i += 1

        return res

class TestSolution(unittest.TestCase):

    def test_romanToInt(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt('III'), 3)
        self.assertEqual(solution.romanToInt('IV'), 4)
        self.assertEqual(solution.romanToInt('IX'), 9)
        self.assertEqual(solution.romanToInt('LVIII'), 58)
        self.assertEqual(solution.romanToInt('MCMXCIV'), 1994)

if __name__ == '__main__':
    unittest.main()
