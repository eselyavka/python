#!/usr/bin/env python

import unittest
from collections import defaultdict


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l, r = 0, 0
        res = []
        for i, letter in enumerate(S):
            if i > r:
                res.append((r - l) + 1)
                l = i

            r = max(r, S.rindex(letter))

            if i == len(S) - 1:
                res.append((r - l) + 1)

        return res


class Solution2(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = defaultdict(list)

        for i, c in enumerate(s):
            last[c].append(i)

        intervals = list(last.values())
        intervals.sort(key=lambda t: t[0])

        merged_intervales = []
        i = 0
        start, end = intervals[0][0], intervals[0][-1]
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i][0], intervals[i][-1]
            if curr_start <= end:
                end = max(end, curr_end)
            else:
                merged_intervales.append([start, end])
                start, end = curr_start, curr_end

        merged_intervales.append([start, end])

        ans = [t[-1] - t[0] + 1 for t in merged_intervales]

        return ans


class TestSolution(unittest.TestCase):

    def test_reverse(self):
        solution = Solution()
        self.assertEqual(solution.partitionLabels('ababcbacadefegdehijhklij'), [9, 7, 8])
        self.assertEqual(solution.partitionLabels('aaaaaa'), [6])
        self.assertEqual(solution.partitionLabels('b'), [1])
        self.assertEqual(solution.partitionLabels('abaccbdeffed'), [6, 6])
        self.assertEqual(solution.partitionLabels('eaaaabaaec'), [9, 1])

        solution2 = Solution2()
        self.assertEqual(solution2.partitionLabels('ababcbacadefegdehijhklij'), [9, 7, 8])
        self.assertEqual(solution2.partitionLabels('aaaaaa'), [6])
        self.assertEqual(solution2.partitionLabels('b'), [1])
        self.assertEqual(solution2.partitionLabels('abaccbdeffed'), [6, 6])
        self.assertEqual(solution2.partitionLabels('eaaaabaaec'), [9, 1])


if __name__ == '__main__':
    unittest.main()
