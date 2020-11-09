#!/usr/bin/env python

import unittest


class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        def is_arithmetic(s):
            s.sort()
            diff = s[1] - s[0]
            for i in range(1, len(s)):
                if s[i] - s[i-1] != diff:
                    return False
            return True

        res = []
        for start, end in zip(l, r):
            res.append(is_arithmetic(nums[start:end+1]))

        return res


class TestSolution(unittest.TestCase):
    def test_checkArithmeticSubarrays(self):
        solution = Solution()
        self.assertEqual(solution.checkArithmeticSubarrays([4, 6, 5, 9, 3, 7],
                                                           [0, 0, 2],
                                                           [2, 3, 5]),
                         [True, False, True])


if __name__ == '__main__':
    unittest.main()
