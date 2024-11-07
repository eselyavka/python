#!/usr/bin/env python

import unittest


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)

        stack = [0]
        ans = [0] * n

        for i in range(1, n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx

            stack.append(i)

        return ans


class TestSolution(unittest.TestCase):
    def test_dailyTemperatures(self):
        solution = Solution()
        self.assertEqual(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
                         [1, 1, 4, 2, 1, 1, 0, 0])


if __name__ == '__main__':
    unittest.main()
