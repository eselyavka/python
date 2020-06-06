#!/usr/bin/env python

import unittest


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_, res = max(candies), []

        for num in candies:
            if num + extraCandies >= max_:
                res.append(True)
            else:
                res.append(False)

        return res


class TestSolution(unittest.TestCase):

    def test_kidsWithCandies(self):
        solution = Solution()
        self.assertListEqual(solution.kidsWithCandies([2, 3, 5, 1, 3], 3),
                             [True, True, True, False, True])


if __name__ == '__main__':
    unittest.main()
