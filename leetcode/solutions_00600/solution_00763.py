#!/usr/bin/env python

import unittest

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
                res.append((r - l)+1)
                l = i

            r = max(r, S.rindex(letter))

            if i == len(S) - 1:
                res.append((r-l) + 1)

        return res

class TestSolution(unittest.TestCase):

    def test_reverse(self):
        solution = Solution()
        self.assertEqual(solution.partitionLabels('ababcbacadefegdehijhklij'), [9, 7, 8])
        self.assertEqual(solution.partitionLabels('aaaaaa'), [6])
        self.assertEqual(solution.partitionLabels('b'), [1])
        self.assertEqual(solution.partitionLabels('abaccbdeffed'), [6, 6])
        self.assertEqual(solution.partitionLabels('eaaaabaaec'), [9, 1])

if __name__ == '__main__':
    unittest.main()
