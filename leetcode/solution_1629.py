#!/usr/bin/env python

import unittest


class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """

        max_ = (releaseTimes[0], keysPressed[0])

        for i in range(1, len(releaseTimes)):
            if (releaseTimes[i] - releaseTimes[i-1] == max_[0] and keysPressed[i] > max_[1]) or releaseTimes[i] - releaseTimes[i-1] > max_[0]:
                max_ = (releaseTimes[i] - releaseTimes[i-1], keysPressed[i])

        return max_[1]


class TestSolution(unittest.TestCase):
    def test_slowestKey(self):
        solution = Solution()
        self.assertEqual(solution.slowestKey([9, 29, 49, 50], 'cbcd'), 'c')


if __name__ == '__main__':
    unittest.main()
