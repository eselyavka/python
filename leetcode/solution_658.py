#!/usr/bin/env python

import unittest

class Solution(object):
    def binary_search(self, arr, target):
        r = len(arr) - 1
        l = 0
        while l <= r:
            mid = (l+r) // 2
            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return mid

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = self.binary_search(arr, x)
        if left == 0:
            return arr[:k]
        elif left == len(arr) - 1:
            return arr[len(arr) - k:]
        else:
            res = []
            right = left + 1
            cnt = 0
            while left >= 0 and right < len(arr) and cnt < k:
                if x - arr[left] <= arr[right] - x:
                    res.append(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
                cnt += 1

            while left >= 0 and cnt < k:
                res.append(arr[left])
                left -= 1
                cnt += 1

            while right < len(arr) and cnt < k:
                res.append(arr[right])
                right += 1
                cnt += 1

        return sorted(res)


class TestSolution(unittest.TestCase):

    def test_findClosestElements(self):
        solution = Solution()
        self.assertListEqual(solution.findClosestElements([1, 2, 3, 4, 5], k=4, x=-1), [1, 2, 3, 4])
        self.assertListEqual(solution.findClosestElements([1, 2, 3, 4, 5], k=2, x=1), [1, 2])
        self.assertListEqual(solution.findClosestElements([1, 2, 3, 4, 5], k=2, x=6), [4, 5])
        self.assertListEqual(solution.findClosestElements([1, 2, 3, 4, 5], k=2, x=5), [4, 5])
        self.assertListEqual(solution.findClosestElements([1, 2, 3, 4, 5], k=4, x=3), [1, 2, 3, 4])
        self.assertListEqual(solution.findClosestElements([1, 2, 4, 5, 6], k=4, x=3), [1, 2, 4, 5])
        self.assertListEqual(solution.findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], k=3, x=5),
                             [3, 3, 4])
        self.assertListEqual(solution.findClosestElements([0, 0, 0, 1, 3, 5, 6, 7, 8, 8], k=2, x=2),
                             [1, 3])
        self.assertListEqual(solution.findClosestElements([0, 2, 2, 3, 4, 6, 7, 8, 9, 9], k=4, x=5),
                             [3, 4, 6, 7])


if __name__ == '__main__':
    unittest.main()
