#!/usr/bin/env python

import unittest

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        def binary_search():
            l = 0
            r = len(A) - 1
            while r >= l:
                mid = (r+l) // 2

                if A[mid - 1] < A[mid] > A[mid+1]:
                    return mid
                elif A[mid-1] < A[mid] < A[mid+1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return binary_search()

class TestSolution(unittest.TestCase):
    def test_peakIndexInMountainArray(self):
        solution = Solution()
        self.assertEqual(solution.peakIndexInMountainArray([0, 1, 0]), 1)
        self.assertEqual(solution.peakIndexInMountainArray([0, 2, 1, 0]), 1)

if __name__ == '__main__':
    unittest.main()
