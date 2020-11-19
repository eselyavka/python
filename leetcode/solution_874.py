#!/usr/bin/env python

import unittest


class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        direction = {0: (0, 1),
                     90: (1, 0),
                     180: (0, -1),
                     270: (-1, 0),
                     -90: (-1, 0),
                     -180: (0, -1),
                     -270: (1, 0)}
        angle = 0
        path = (0, 0)
        res = float('-inf')
        obstacle_set = set(map(tuple, obstacles))
        for cmd in commands:
            # reset angle
            if abs(angle) == 360:
                angle = 0
            if cmd in [-1, -2]:
                angle = (angle + 90) if cmd == -1 else (angle - 90)
            else:
                x, y = path
                x_i, y_i = direction[angle]

                for _ in xrange(cmd):
                    x += x_i
                    y += y_i
                    if (x, y) in obstacle_set:
                        break
                    path = (x, y)

                res = max(res, path[0]**2 + path[1]**2)
        return res


class TestSolution(unittest.TestCase):

    def test_robotSim(self):
        solution = Solution()
        self.assertEqual(solution.robotSim([4, -1, 4, -2, 4], [[2, 4]]), 65)


if __name__ == '__main__':
    unittest.main()
