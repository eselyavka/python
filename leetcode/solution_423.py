#!/usr/bin/env python

import unittest


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        digits = {0: "zero",
         1: "one",
         2: "two",
         3: "three",
         4: "four",
         5: "five",
         6: "six",
         7: "seven",
         8: "eight",
         9: "nine"}
        immutable = sum([ord(c) for c in s])
        ss = immutable
        i,j = 0, 0
        res = []
        while ss != 0:
            digit_sum = sum([ord(x) for x in digits[i]])
            print i, digit_sum
            ss -= digit_sum
            if ss < 0:
                j += 1
                i = j
                ss = immutable
                res = []
                continue
            else:
                res.append(i)
            i += 1

        return ''.join([str(c) for c in res])


class TestSolution(unittest.TestCase):
    def test_originalDigits(self):
        solution = Solution()
        self.assertEqual(solution.originalDigits("zerozero"), "00")
        self.assertEqual(solution.originalDigits("zroe"), "0")
        self.assertEqual(solution.originalDigits("eon"), "1")
        self.assertEqual(solution.originalDigits("owoztneoer"), "012")
        self.assertEqual(solution.originalDigits("fviefuro"), "45")


if __name__ == '__main__':
    unittest.main()
