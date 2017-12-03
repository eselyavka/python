#!/usr/bin/env python

import unittest

class Solution(object):
    def _rec(self, num, arr):
        if num == 0:
            return int(''.join([str(x) for x in arr[::-1]])) if arr else 0
        rem = abs(num)%7
        arr.append(rem)
        return self._rec(abs(num)/7, arr)

    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        mas = list()
        res = self._rec(num, mas) * -1 if num < 0 else self._rec(num, mas)
        return str(res)

class TestSolution(unittest.TestCase):

    def test_convertToBase7(self):
        nums = [100, -7, 0]
        solution = Solution()
        self.assertEqual(solution.convertToBase7(nums[0]), "202")
        self.assertEqual(solution.convertToBase7(nums[1]), "-10")
        self.assertEqual(solution.convertToBase7(nums[2]), "0")

if __name__ == '__main__':
    unittest.main()
