#!/usr/bin/env python

import unittest


class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        if label == 1:
            return [1]

        res = [label]

        level = 0
        while 2**level <= label:
            level += 1

        while level > 1:
            offset = ((2 ** level - 1) - label)
            level -= 1
            label = (2**level + offset)//2
            res.insert(0, label)

        return res


class TestSolution(unittest.TestCase):
    def test_pathInZigZagTree(self):
        solution = Solution()
        self.assertListEqual(solution.pathInZigZagTree(14), [1, 3, 4, 14])


if __name__ == '__main__':
    unittest.main()
