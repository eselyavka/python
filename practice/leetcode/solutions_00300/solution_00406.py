#!/usr/bin/env python3

"""LeetCode solution 00406."""

import unittest

class Solution(object):

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        d, height, res = {}, set(), []

        for e in people:
            if e[0] in d:
                d[e[0]] += [e[1]]
            else:
                d[e[0]] = [e[1]]

            height.add(e[0])

        for h in sorted(height)[::-1]:
            for k in sorted(d[h]):
                res.insert(k, [h, k])
        return res

class TestSolution(unittest.TestCase):

    def test_reconstructQueue(self):
        people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        people2 = [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7],
                   [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]

        solution = Solution()
        self.assertEqual(solution.reconstructQueue(people),
                         [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]])
        self.assertEqual(solution.reconstructQueue(people2),
                         [[3, 0], [6, 0], [7, 0], [5, 2], [3, 4],
                          [5, 3], [6, 2], [2, 7], [9, 0], [1, 9]])

if __name__ == '__main__':
    unittest.main()
