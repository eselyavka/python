#!/usr/bin/env python

import unittest


class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) < k:
            return s

        stack = list()

        for c in s:
            if stack and c == stack[-1][0]:
                node = stack.pop()
                if node[1] < k - 1:
                    stack.append((c, node[1] + 1))
            else:
                stack.append((c, 1))

        return ''.join([t[0]*t[1] for t in stack])


class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        solution = Solution()
        self.assertEqual(solution.removeDuplicates("deeedbbcccbdaa", 3), "aa")


if __name__ == '__main__':
    unittest.main()
