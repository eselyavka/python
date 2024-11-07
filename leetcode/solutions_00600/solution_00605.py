#!/usr/bin/env python

import unittest

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1:
            if n == 1:
                return flowerbed[0] == 0
            elif n == 0:
                return True
            else:
                return False

        res = 0
        for i in range(len(flowerbed)):
            if i == len(flowerbed) - 1:
                if flowerbed[i] != 1 and flowerbed[i - 1] != 1:
                    flowerbed[i] = 1
                    res += 1
            elif i == 0:
                if flowerbed[i] != 1 and flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    res += 1
            else:
                if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    res += 1

        return res >= n

class TestSolution(unittest.TestCase):

    def test_canPlaceFlowers(self):
        flowerbed = [1, 0, 0, 0, 1]
        flowerbed2 = [0]
        flowerbed3 = [1]
        flowerbed4 = [1, 0, 0]
        flowerbed5 = [0, 0]
        flowerbed6 = [0, 1]
        flowerbed7 = [1, 0, 0, 0, 1]
        flowerbed8 = [1]
        solution = Solution()
        self.assertTrue(solution.canPlaceFlowers(flowerbed, 1))
        self.assertFalse(solution.canPlaceFlowers(flowerbed, 2))
        self.assertTrue(solution.canPlaceFlowers(flowerbed2, 1))
        self.assertFalse(solution.canPlaceFlowers(flowerbed3, 1))
        self.assertTrue(solution.canPlaceFlowers(flowerbed4, 1))
        self.assertTrue(solution.canPlaceFlowers(flowerbed5, 1))
        self.assertFalse(solution.canPlaceFlowers(flowerbed5, 2))
        self.assertFalse(solution.canPlaceFlowers(flowerbed6, 1))
        self.assertFalse(solution.canPlaceFlowers(flowerbed7, 2))
        self.assertTrue(solution.canPlaceFlowers(flowerbed8, 0))

if __name__ == '__main__':
    unittest.main()
