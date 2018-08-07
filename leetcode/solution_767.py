#!/usr/bin/env python

import unittest
import heapq

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) == 1:
            return S

        if len(S) == 2:
            return S if len(S) == len(set(S)) else ''

        d, pq = dict(), []

        for c in S:
            if d.get(c):
                d[c] += -1
            else:
                d[c] = -1

        for x in d.iteritems():
            heapq.heappush(pq, [x[1], x[0]])

        prev, res = None, ''

        while pq:
            curr = heapq.heappop(pq)
            res += curr[1]
            curr[0] += 1

            if prev and prev[0] < 0:
                heapq.heappush(pq, prev)

            prev = curr

        return res if len(res) == len(S) else ''

class TestSolution(unittest.TestCase):
    def test_reorganizeString(self):
        solution = Solution()
        self.assertEqual(solution.reorganizeString("aaab"), "")
        self.assertEqual(solution.reorganizeString("abbabbaaab"), "ababababab")
        self.assertEqual(solution.reorganizeString("a"), "a")
        self.assertEqual(solution.reorganizeString("aa"), "")
        self.assertEqual(solution.reorganizeString("ab"), "ab")
        self.assertEqual(solution.reorganizeString("aab"), "aba")
        self.assertEqual(solution.reorganizeString("aaab"), "")
        self.assertEqual(solution.reorganizeString("vvvlo"), "vlvov")
        self.assertEqual(solution.reorganizeString("blflxll"), "lblflxl")

if __name__ == '__main__':
    unittest.main()
