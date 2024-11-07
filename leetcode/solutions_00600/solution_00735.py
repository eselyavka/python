#!/usr/bin/env python

import unittest


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if len(asteroids) <= 1:
            return asteroids

        s = []

        for num in asteroids:
            if num > 0:
                s.append(num)
            else:
                while s and s[-1] > 0 and s[-1] < abs(num):
                    s.pop()
                if not s or s[-1] < 0:
                    s.append(num)
                if s[-1] == -num:
                    s.pop()
        return s


class TestSolution(unittest.TestCase):
    def test_asteroidCollision(self):
        solution = Solution()
        self.assertListEqual(solution.asteroidCollision([5, 10, -5]), [5, 10])


if __name__ == '__main__':
    unittest.main()
