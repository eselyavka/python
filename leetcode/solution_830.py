#!/usr/bin/env python

import unittest

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if not S or len(S) <= 2:
            return []

        cnt, res, i = 0, [], None
        for i in range(1, len(S)):
            if S[i-1] == S[i]:
                cnt += 1
            else:
                if cnt >= 2:
                    res.append([i - 1 - cnt, i - 1])
                cnt = 0

        if cnt >= 2:
            res.append([i - cnt, i])

        return res

class TestSolution(unittest.TestCase):
    def test_largeGroupPositions(self):
        solution = Solution()
        self.assertEqual(solution.largeGroupPositions("abbxxxxzzy"), [[3, 6]])
        self.assertEqual(solution.largeGroupPositions("bbbxxzzy"), [[0, 2]])
        self.assertEqual(solution.largeGroupPositions("abc"), [])
        self.assertEqual(solution.largeGroupPositions("abcdddeeeeaabbbcd"),
                         [[3, 5], [6, 9], [12, 14]])
        self.assertEqual(solution.largeGroupPositions(""), [])
        self.assertEqual(solution.largeGroupPositions("aa"), [])
        self.assertEqual(solution.largeGroupPositions("aaa"), [[0, 2]])
        self.assertEqual(solution.largeGroupPositions("qwasdcaaa"), [[6, 8]])
        self.assertEqual(solution.largeGroupPositions("qqqaaabbb"), [[0, 2], [3, 5], [6, 8]])


if __name__ == '__main__':
    unittest.main()
