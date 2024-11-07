#!/usr/bin/env python

import unittest

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = {B[i]:i for i in range(len(B))}
        res = []

        for num in A:
            res.append(d[num])

        return res

class TestSolution(unittest.TestCase):
    def test_anagramMappings(self):
        solution = Solution()
        self.assertEqual(solution.anagramMappings([12, 28, 46, 32, 50],
                                                  [50, 12, 32, 46, 28]),
                         [1, 4, 3, 2, 0])

if __name__ == '__main__':
    unittest.main()
