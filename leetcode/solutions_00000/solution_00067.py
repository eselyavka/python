#!/usr/bin/env python

import unittest


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a

        if a[-1] == b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1] == b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'

        return self.addBinary(a[:-1], b[:-1]) + '1'


class Solution2(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ii = len(a) - 1
        jj = len(b) - 1
        if ii < jj:
            a = '0'*(jj-ii) + a
        elif ii > jj:
            b = '0'*(ii-jj) + b

        i = len(a) - 1
        j = len(b) - 1
        carry_flag, res = False, ''
        while i >= 0 and j >= 0:
            if a[i] == '1' and b[j] == '1':
                if carry_flag:
                    res = '1' + res
                else:
                    res = '0' + res
                carry_flag = True
            elif a[i] == '1' or b[j] == '1':
                if carry_flag:
                    res = '0' + res
                    carry_flag = True
                else:
                    res = '1' + res
            else:
                if carry_flag:
                    res = '1' + res
                else:
                    res = '0' + res
                carry_flag = False
            i -= 1
            j -= 1

        return res if not carry_flag else '1' + res


class TestSolution(unittest.TestCase):
    def test_addBinary(self):
        solution = Solution()
        self.assertEqual(solution.addBinary("1010", "1011"), "10101")
        self.assertEqual(solution.addBinary("11", "1"), "100")

        solution2 = Solution()
        self.assertEqual(solution2.addBinary("1010", "1011"), "10101")
        self.assertEqual(solution2.addBinary("11", "1"), "100")


if __name__ == '__main__':
    unittest.main()
