#!/usr/bin/python

import unittest


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 1:
            return 0 if (gas[0] - cost[0]) >= 0 else -1

        sum_, idx, t = [0] * 3
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            t = t + diff
            if t < 0:
                idx, t = i+1, 0
            sum_ += diff

        if sum_ < 0:
            return -1

        return idx


class TestSolution(unittest.TestCase):

    def test_canCompleteCircuit(self):
        solution = Solution()
        self.assertEqual(solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
        self.assertEqual(solution.canCompleteCircuit([5, 5, 1, 3, 4], [8, 1, 7, 1, 1]), 3)
        self.assertEqual(solution.canCompleteCircuit([2], [2]), 0)
        self.assertEqual(solution.canCompleteCircuit([3, 1, 1], [1, 2, 2]), 0)
        self.assertEqual(solution.canCompleteCircuit([3, 3, 4], [3, 4, 4]), -1)


if __name__ == '__main__':
    unittest.main()
