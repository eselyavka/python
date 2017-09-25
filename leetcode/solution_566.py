#!/usr/bin/env python

import unittest

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        vector = reduce(lambda x, y: x+y, nums)

        if len(vector) != r * c:
            return nums

        reshaped = list()

        for i in range(r):
            reshaped.append([])
            for j in range(c):
                reshaped[i].append(vector[i*c + j])
        return reshaped


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.arr = [[1, 2], [3, 4]]
        self.arr2 = [[1], [2], [3], [4]]

    def test_matrixReshape_success(self):
        solution = Solution()
        self.assertListEqual(solution.matrixReshape(self.arr, 1, 4), [[1, 2, 3, 4]])
        self.assertListEqual(solution.matrixReshape(self.arr2, 2, 2), [[1, 2], [3, 4]])

    def test_matrixReshape_failure(self):
        solution = Solution()
        self.assertListEqual(solution.matrixReshape(self.arr, 2, 4), self.arr)

if __name__ == '__main__':
    unittest.main()
