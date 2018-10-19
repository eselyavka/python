#!/usr/bin/env python

import unittest
from collections import defaultdict
import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if len(tasks) == 1:
            return 1

        d = defaultdict(int)
        for task in tasks:
            d[task] -= 1

        heap = []

        for item in d.iteritems():
            heapq.heappush(heap, [item[1], item[0]])

        res = 0
        n += 1
        while heap:
            stack = []
            cnt = 0
            for _ in range(n):
                if heap:
                    cnt += 1
                    curr = heapq.heappop(heap)
                    if curr[0] + 1 < 0:
                        curr[0] += 1
                        stack.append(curr)

            for item in stack:
                heapq.heappush(heap, item)

            res += n if heap else cnt

        return res

class TestSolution(unittest.TestCase):
    def test_leastInterval(self):
        solution = Solution()
        self.assertEqual(solution.leastInterval(["A", "A", "A", "B", "B", "B"], 2), 8)

if __name__ == '__main__':
    unittest.main()
