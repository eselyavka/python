#!/usr/bin/env python3

"""LeetCode solution 00752."""

import unittest
from collections import deque


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if target == "0000":
            return 0

        dead = set(deadends)
        if "0000" in dead or target in dead:
            return -1

        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            state, steps = queue.popleft()

            for neighbor in self.neighbors(state):
                if neighbor in dead or neighbor in visited:
                    continue

                if neighbor == target:
                    return steps + 1

                visited.add(neighbor)
                queue.append((neighbor, steps + 1))

        return -1

    def neighbors(self, state):
        for i in range(4):
            digit = int(state[i])

            for move in (-1, 1):
                new_digit = (digit + move) % 10
                yield state[:i] + str(new_digit) + state[i + 1:]


class TestSolution(unittest.TestCase):
    def test_openLock(self):
        solution = Solution()

        self.assertEqual(
            solution.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"),
            6,
        )
        self.assertEqual(solution.openLock(["8888"], "0009"), 1)
        self.assertEqual(
            solution.openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"),
            -1,
        )
        self.assertEqual(solution.openLock(["0000"], "8888"), -1)
        self.assertEqual(solution.openLock([], "0000"), 0)


if __name__ == '__main__':
    unittest.main()
