#!/usr/bin/env python

import unittest


class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        i, cnt = 0, 0
        while len(res) != len(nums):
            if cnt % 2 == 1:
                res.append(nums[n])
                n += 1
            else:
                res.append(nums[i])
                i += 1
            cnt += 1

        return res


class TestSolution(unittest.TestCase):
    def test_shuffle(self):
        solution = Solution()
        self.assertListEqual(solution.shuffle([2, 5, 1, 3, 4, 7], 3), [2, 3, 5, 4, 1, 7])


if __name__ == '__main__':
    unittest.main()
