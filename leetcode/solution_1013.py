#!/usr/bin/env python

import unittest

class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        sum_ = sum(A)
        if sum_ % 3 != 0:
            return False

        s, cnt = 0, 0
        target = sum_ / 3
        for num in A:
            s += num

            if s == target:
                cnt += 1
                s = 0
            else:
                continue

            if cnt == 3:
                return True

        return False


class TestSolution(unittest.TestCase):
    def test_canThreePartsEqualSum(self):
        solution = Solution()
        self.assertTrue(solution.canThreePartsEqualSum([1, 1, 1]))
        self.assertTrue(solution.canThreePartsEqualSum([0, 0, 0]))
        self.assertFalse(solution.canThreePartsEqualSum([0, 0, 10]))
        self.assertTrue(solution.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
        self.assertFalse(solution.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
        self.assertTrue(solution.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
        self.assertFalse(solution.canThreePartsEqualSum([6, 1, 1, 13, -1, 0, -10, 20]))
        self.assertTrue(solution.canThreePartsEqualSum(
            [29, 31, 27, -10, -67, 22, 15, -1, -16, -29, 59, -18, 48]))


if __name__ == '__main__':
    unittest.main()
