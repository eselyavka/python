#!/usr/bin/env python

import unittest

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return []


        r = 0
        l = len(A) - 1
        A.sort(key=lambda x: x % 2 == 1)
        while l >= r:
            if not all([A[r] % 2 == 0 and r % 2 == 0,
                        A[l] % 2 == 1 and l % 2 == 1]):
                A[r], A[l] = A[l], A[r]
            r += 1
            l -= 1

        return A

class TestSolution(unittest.TestCase):
    def test_sortArrayByParityII(self):
        solution = Solution()
        self.assertEqual(solution.sortArrayByParityII([4, 2, 5, 7]), [4, 5, 2, 7])
        self.assertEqual(solution.sortArrayByParityII([4, 2, 6, 5, 7, 3]), [4, 7, 6, 5, 2, 3])


if __name__ == '__main__':
    unittest.main()
