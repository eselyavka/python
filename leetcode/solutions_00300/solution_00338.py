#!/usr/bin/env python

import unittest


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = list()
        for i in range(num + 1):
            res.append(sum([int(x) for x in bin(i)[2:]]))
        return res

class TestSolution(unittest.TestCase):

    def test_countBits(self):
        solution = Solution()
        self.assertListEqual(solution.countBits(2), [0, 1, 1])
        self.assertListEqual(solution.countBits(5), [0, 1, 1, 2, 1, 2])

if __name__ == '__main__':
    unittest.main()
