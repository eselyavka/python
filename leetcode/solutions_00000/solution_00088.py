#!/usr/bin/env python

import unittest

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2, l = m-1, n-1, (m+n)-1
        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] > nums2[idx2]:
                nums1[l] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[l] = nums2[idx2]
                idx2 -= 1
            l -= 1
        while idx2 >= 0:
            nums1[l] = nums2[idx2]
            l, idx2 = l - 1, idx2 - 1

class TestSolution(unittest.TestCase):

    def test_merge(self):
        solution = Solution()

        arr1 = [1, 2, 3, 0, 0, 0]
        arr2 = [2, 5, 6]

        solution.merge(arr1, 3, arr2, 3)

        self.assertEqual(arr1, [1, 2, 2, 3, 5, 6])

if __name__ == '__main__':
    unittest.main()
