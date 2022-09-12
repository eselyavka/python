#!/usr/bin/env python

import unittest


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        i, j = 0, 0
        res = []

        while i < n and j < m:
            if nums1[i] > nums2[j]:
                res.append(nums2[j])
                j += 1
            else:
                res.append(nums1[i])
                i += 1

        while i < n:
            res.append(nums1[i])
            i+=1

        while j < m:
            res.append(nums2[j])
            j+=1

        mid = len(res)//2

        return res[mid] if len(res) % 2 == 1 else (res[mid - 1] + res[mid]) / 2.0


class TestSolution(unittest.TestCase):
    def test_findMedianSortedArrays(self):
        solution = Solution()

        self.assertEqual(solution.findMedianSortedArrays([1, 3], [2]), 2.0)


if __name__ == '__main__':
    unittest.main()
