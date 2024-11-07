#!/usr/bin/env python

import unittest


class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        s = len(rating)
        res = 0
        for i in range(s):
            for j in range(i+1, s):
                for k in range(j+1, s):
                    if rating[i] > rating[j] > rating[k]:
                        res += 1
                    if rating[i] < rating[j] < rating[k]:
                        res += 1
        return res


class TestSolution(unittest.TestCase):

    def test_numTeams(self):
        solution = Solution()
        self.assertEqual(solution.numTeams([2, 5, 3, 4, 1]), 3)


if __name__ == '__main__':
    unittest.main()
