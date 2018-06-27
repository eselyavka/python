#!/usr/bin/env python

import unittest

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        i = 0
        queue = rooms[i]
        visited = set([i])
        while queue:
            room_num = queue.pop()
            if room_num not in visited:
                visited.add(room_num)
                queue.extend(set(rooms[room_num]) - visited)

        return len(visited) == len(rooms)

class TestSolution(unittest.TestCase):
    def test_canVisitAllRooms(self):
        solution = Solution()
        self.assertTrue(solution.canVisitAllRooms([[1], [2], [3], []]))
        self.assertFalse(solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))

if __name__ == '__main__':
    unittest.main()
