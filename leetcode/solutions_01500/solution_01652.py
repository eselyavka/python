#!/usr/bin/env python

import unittest


class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """

        n = len(code)

        if k == 0:
            return [0] * n

        res = []
        if k > 0:
            for i in range(n):
                j = 1
                acc = 0
                for _ in range(k):
                    idx = (i + j) % n
                    j += 1
                    acc += code[idx]
                res.append(acc)
        if k < 0:
            for i in range(n):
                j = -1
                acc = 0
                for _ in range(abs(k)):
                    idx = (i + j) % n
                    j -= 1
                    acc += code[idx]
                res.append(acc)
        return res


class TestSolution(unittest.TestCase):
    def test_decrypt(self):
        solution = Solution()
        self.assertEqual(solution.decrypt([5, 7, 1, 4], 3), [12, 10, 16, 13])


if __name__ == '__main__':
    unittest.main()
