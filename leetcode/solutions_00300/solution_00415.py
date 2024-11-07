#!/usr/bin/env python

import unittest


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def atoi(s):
            res, i = 0, 0
            for c in reversed(s):
                res += int(c) * (10 ** i)
                i += 1

            return res

        def itoa(num):
            s = []
            while True:
                s.append(chr(ord('0') + num % 10))
                num //= 10
                if num == 0:
                    break

            return ''.join(reversed(s))

        return itoa(atoi(num1) + atoi(num2))


class TestSolution(unittest.TestCase):

    def test_addStrings(self):
        solution = Solution()
        self.assertEqual(solution.addStrings('124', '34'), '158')


if __name__ == '__main__':
    unittest.main()
