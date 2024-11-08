#!/usr/bin/env python

import unittest


class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.idx_map = {}

        for idx, num in enumerate(nums):
            if num:
                self.idx_map[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res = 0
        for idx in self.idx_map:
            res += self.idx_map[idx] * vec.idx_map.get(idx, 0)

        return res


class TestSolution(unittest.TestCase):
    def test_SparseVector(self):
        v1 = SparseVector([1, 0, 0, 2, 3])
        v2 = SparseVector([0, 3, 0, 4, 0])
        self.assertEqual(v1.dotProduct(v2), 8)


if __name__ == '__main__':
    unittest.main()
