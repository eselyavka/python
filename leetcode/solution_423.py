#!/usr/bin/env python

import unittest


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = [0]*10
        for c in s:
            if c == 'z':
                counter[0] += 1
            if c == 'o': # 0;1;2;4
                counter[1] += 1
            if c == 'w':
                counter[2] += 1
            if c == 'h': # 8
                counter[3] += 1
            if c == 'u':
                counter[4] += 1
            if c == 'f': # 4
                counter[5] += 1
            if c == 'x':
                counter[6] += 1
            if c == 's': # 6
                counter[7] += 1
            if c == 'g':
                counter[8] += 1
            if c == 'i': #8; 6; 5
                counter[9] += 1

        counter[3] -= counter[8]
        counter[5] -= counter[4]
        counter[7] -= counter[6]

        counter[1] -= (counter[0] + counter[2] + counter[4])
        counter[9] -= (counter[8] + counter[6] + counter[5])

        return ''.join([str(x) * counter[x] for x in range(len(counter)) if counter[x]])


class TestSolution(unittest.TestCase):
    def test_originalDigits(self):
        solution = Solution()
        self.assertEqual(solution.originalDigits("zerozero"), "00")
        self.assertEqual(solution.originalDigits("zroe"), "0")
        self.assertEqual(solution.originalDigits("eon"), "1")
        self.assertEqual(solution.originalDigits("owoztneoer"), "012")
        self.assertEqual(solution.originalDigits("fviefuro"), "45")
        self.assertEqual(solution.originalDigits("esnve"), "7")
        self.assertEqual(solution.originalDigits("zeroonetwothreefourfivesixseveneightnine"),
                         "0123456789")


if __name__ == '__main__':
    unittest.main()
