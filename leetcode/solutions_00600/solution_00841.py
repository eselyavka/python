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


class Solution2(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        s = [rooms[0]]
        visited = [False for _ in range(len(rooms))]
        visited[0] = True

        while s:
            cnt = len(s)
            while cnt:
                nodes = s.pop()
                for node in nodes:
                    if visited[node]:
                        continue

                    visited[node] = True
                    s += [rooms[node]]

                cnt -= 1

        return all(visited)


class TestSolution(unittest.TestCase):
    def test_canVisitAllRooms(self):
        solution = Solution()
        self.assertTrue(solution.canVisitAllRooms([[1], [2], [3], []]))
        self.assertFalse(solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))

        solution = Solution2()
        self.assertTrue(solution.canVisitAllRooms([[1], [2], [3], []]))
        self.assertFalse(solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))


if __name__ == '__main__':
    unittest.main()
