#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d, i = defaultdict(int), 0

        while i < len(list1):
            d[list1[i]] = i
            i += 1

        i, _min = 0, float('+inf')
        res = []

        while i < len(list2):
            if list2[i] in d:
                if _min > (i+d[list2[i]]):
                    res = [list2[i]]
                    _min = i+d[list2[i]]
                elif _min == (i+d[list2[i]]):
                    res.append(list2[i])
            i += 1

        return res

class TestSolution(unittest.TestCase):

    def test_findRestaurant(self):
        solution = Solution()

        self.assertListEqual(solution.findRestaurant(["Shogun",
                                                      "Tapioca Express",
                                                      "Burger King",
                                                      "KFC"],
                                                     ["Piatti",
                                                      "The Grill at Torrey Pines",
                                                      "Hungry Hunter Steakhouse",
                                                      "Shogun"]),
                             ["Shogun"])

if __name__ == '__main__':
    unittest.main()
