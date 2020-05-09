#!/usr/bin/env python

import unittest
from collections import Counter


class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id_, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        visited, bfs = set([id_]), [id_]
        local_level, friend_at_level = 1, []
        while local_level <= level:
            size = len(bfs)
            while size:
                for idx in friends[bfs.pop()]:
                    if idx in visited:
                        continue
                    bfs.append(idx)
                    if local_level == level:
                        friend_at_level.append(idx)
                visited |= set(bfs)
                size -= 1
            local_level += 1

        watched = Counter()
        for friend in friend_at_level:
            for video in watchedVideos[friend]:
                watched[video] += 1

        return sorted(watched.keys(), key=lambda k: (watched[k], k))


class TestSolution(unittest.TestCase):

    def test_watchedVideosByFriends(self):
        solution = Solution()
        self.assertListEqual(solution.watchedVideosByFriends(
            [["A", "B"],
             ["C"],
             ["B", "C"],
             ["D"]],
            [[1, 2],
             [0, 3],
             [0, 3],
             [1, 2]], 0, 1), ["B", "C"])


if __name__ == '__main__':
    unittest.main()
