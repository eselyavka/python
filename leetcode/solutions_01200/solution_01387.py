#!/usr/bin/env python

import unittest


class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        if lo == hi == 1:
            return 1

        res = []
        for num in range(lo, hi+1):
            steps = 0
            data = num
            while num != 1:
                if num % 2 == 0:
                    num = num // 2
                else:
                    num = 3 * num + 1
                steps += 1

            res.append(tuple([data, steps]))

        res.sort(key=lambda t: t[1])

        return res[k-1][0]


class TestSolution(unittest.TestCase):
    def test_getKth(self):
        solution = Solution()
        self.assertEqual(solution.getKth(12, 15, 2), 13)


if __name__ == '__main__':
    unittest.main()
