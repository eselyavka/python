#!/usr/bin/env python

import unittest

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

class TestSolution(unittest.TestCase):

    def test_intersection(self):
        solution = Solution()

        self.assertEqual(solution.intersection([1, 2, 2, 1], [2, 2]), [2])

if __name__ == '__main__':
    unittest.main()
