#!/usr/bin/env python

import unittest

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return bits[0] == 0

        start, i = 0, 0

        while i < len(bits):
            start = i
            if bits[i] != 0:
                i += 2
            else:
                i += 1

        return start == len(bits) - 1

class TestSolution(unittest.TestCase):

    def test_isOneBitCharacter(self):
        solution = Solution()

        self.assertTrue(solution.isOneBitCharacter([1, 0, 0]))
        self.assertFalse(solution.isOneBitCharacter([1, 1, 1, 0]))
        self.assertTrue(solution.isOneBitCharacter([0, 0]))

if __name__ == '__main__':
    unittest.main()
