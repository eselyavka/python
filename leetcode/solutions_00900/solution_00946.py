#!/usr/bin/env python

import unittest


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack, i = [], 0
        for e in pushed:
            stack.append(e)
            while stack and stack[-1] == popped[i]:
                i += 1
                stack.pop()

        return len(stack) == 0


class TestSolution(unittest.TestCase):
    def test_validateStackSequences(self):
        solution = Solution()
        self.assertTrue(solution.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))


if __name__ == '__main__':
    unittest.main()
