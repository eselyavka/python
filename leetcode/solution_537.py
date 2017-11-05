#!/usr/bin/env python

import unittest


class Solution(object):
    def _mult(self, number, nums):
        res = []
        for num in nums:
            if 'i' in num and 'i' in number:
                res.append(str(int(num[:-1]) * int(number[:-1]) * -1))
            elif 'i' in num:
                res.append(str(int(num[:-1]) * int(number)) + 'i')
            elif 'i' in number:
                res.append(str(int(num) * int(number[:-1])) + 'i')
            else:
                res.append(str(int(num) * int(number)))
        return res

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_split = a.split('+')
        b_split = b.split('+')

        res = []
        for part in a_split:
            res += self._mult(part, b_split)

        real = str(sum([int(x) for x in res if 'i' not in x]))
        imagine = str(sum([int(x[:-1]) for x in res if 'i' in x])) + 'i'
        return real + '+' + imagine

class TestSolution(unittest.TestCase):

    def test_complexNumberMultiply(self):
        solution = Solution()
        self.assertEqual(solution.complexNumberMultiply('1+1i', '1+1i'), '0+2i')
        self.assertEqual(solution.complexNumberMultiply('1+-1i', '1+-1i'), '0+-2i')

if __name__ == '__main__':
    unittest.main()
