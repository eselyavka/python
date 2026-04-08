#!/usr/bin/env python3

"""LeetCode solution 00874."""

import unittest


class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obstacles_set = set((x, y) for x, y in obstacles)
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]
        direction_index = 0
        x = 0
        y = 0
        max_distance = 0

        for command in commands:
            if command == -1:
                direction_index = (direction_index + 1) % 4
                continue

            if command == -2:
                direction_index = (direction_index - 1) % 4
                continue

            dx, dy = directions[direction_index]
            while command > 0:
                next_x = x + dx
                next_y = y + dy
                if (next_x, next_y) in obstacles_set:
                    break

                x = next_x
                y = next_y
                max_distance = max(max_distance, x * x + y * y)
                command -= 1

        return max_distance


class TestSolution(unittest.TestCase):

    def test_robotSim(self):
        solution = Solution()
        self.assertEqual(solution.robotSim([4, -1, 3], []), 25)
        self.assertEqual(solution.robotSim([4, -1, 4, -2, 4], [[2, 4]]), 65)
        self.assertEqual(solution.robotSim([-1, -2, -1, -2], []), 0)


if __name__ == '__main__':
    unittest.main()
