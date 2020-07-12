#!/usr/bin/env python

import unittest


class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []

        for idx, num in zip(index, nums):
            if idx == len(target):
                target.append(num)
            else:
                target = target[:idx] + [num] + target[idx:]

        return target


class TestSolution(unittest.TestCase):
    def test_createTargetArray(self):
        solution = Solution()
        self.assertListEqual(solution.createTargetArray([0, 1, 2, 3, 4],
                                                        [0, 1, 2, 2, 1]),
                             [0, 4, 1, 3, 2])


if __name__ == '__main__':
    unittest.main()
