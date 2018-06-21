#!/usr/bin/env python

import unittest

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []

        nums1.sort()
        nums2.sort()

        def binary_search(arr, elem):
            r = 0
            l = len(arr) - 1

            while r <= l:
                mid = (r+l)//2
                if arr[mid] == elem:
                    return mid
                elif elem > arr[mid]:
                    r = mid + 1
                else:
                    l = mid - 1
            return -1

        i = len(nums1) - 1

        while i >= 0:
            idx = binary_search(nums2, nums1[i])
            if idx != -1:
                del nums2[idx]
            else:
                del nums1[i]
            i -= 1

        return nums1

class TestSolution(unittest.TestCase):
    def test_intersect(self):
        solution = Solution()
        self.assertEqual(solution.intersect([], []), [])
        self.assertEqual(solution.intersect([1, 2, 2, 1], [2, 2]), [2, 2])
        self.assertEqual(solution.intersect([1], [1, 1]), [1])
        self.assertEqual(solution.intersect([1, 2], [1, 1]), [1])

if __name__ == '__main__':
    unittest.main()
