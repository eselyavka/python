#!/usr/bin/env python

import unittest
from collections import defaultdict, Counter
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        res = d.items()

        if 'heapq' in globals():
            return [x[0] for x in heapq.nlargest(k, res, key=lambda x: x[1])]

        res.sort(key=lambda x: x[1])
        return [x[0] for x in res[:-(k + 1):-1]]


class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res


class TestSolution(unittest.TestCase):

    def test_topKFrequent(self):
        solution = Solution()

        arr = [4, 5, 1, 1, 1, 2, 2, 3]

        self.assertEqual(solution.topKFrequent(arr, 2),
                         [1, 2])

        solution2 = Solution2()
        self.assertEqual(sorted(solution2.topKFrequent(arr, 2)),
                         [1, 2])


if __name__ == '__main__':
    unittest.main()
