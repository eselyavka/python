#!/usr/bin/env python

import unittest
import heapq


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if len(arr) == 1:
            arr[0] = -1
            return arr

        if len(arr) == 2:
            arr[0] = arr[1]
            arr[1] = -1
            return arr

        h = []
        for i, num in enumerate(arr):
            heapq.heappush(h, (-num, i))

        element, max_i = heapq.heappop(h)
        i = 0
        while i < len(arr) - 2:
            if i < max_i:
                arr[i] = element * -1
                i += 1
            else:
                element, max_i = heapq.heappop(h)

        arr[-2] = arr[-1]
        arr[-1] = -1

        return arr


class TestSolution(unittest.TestCase):
    def test_replaceElements(self):
        solution = Solution()
        self.assertListEqual(solution.replaceElements([17, 18, 5, 4, 6, 1]), [18, 6, 6, 6, 1, -1])


if __name__ == '__main__':
    unittest.main()
