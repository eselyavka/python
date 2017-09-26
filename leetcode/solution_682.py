#!/usr/bin/env python

import unittest

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """

        points = list()

        for operation in ops:
            if operation == '+':
                points.append(sum(points[-2:]))
            elif operation == 'D':
                points.append(points[-1]*2)
            elif operation == 'C':
                points.pop()
            else:
                points.append(int(operation))
        return sum(points)

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.record1 = ["5", "2", "C", "D", "+"]
        self.record2 = ["5", "-2", "4", "C", "D", "9", "+", "+"]

    def test_calPoints(self):
        solution = Solution()
        self.assertEqual(solution.calPoints(self.record1), 30)
        self.assertEqual(solution.calPoints(self.record2), 27)

if __name__ == '__main__':
    unittest.main()
