#!/usr/bin/env python


import unittest


class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        d = dict()

        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            if idx in d:
                d[idx] = i - d[idx] - 1
            else:
                d[idx] = i

        for idx in d:
            if distance[idx] != d[idx]:
                return False

        return True


class TestSolution(unittest.TestCase):
    def test_checkDistances(self):
        solution = Solution()
        self.assertTrue(solution.checkDistances("abaccb",
                                                [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                 0, 0]))


if __name__ == '__main__':
    unittest.main()
