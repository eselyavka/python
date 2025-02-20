#!/usr/bin/env python

import unittest


class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        self.ans = ""
        self.found = False

        seen = set(nums)

        def generate_permutations(chars, n, current=""):
            if self.found:
                return

            if n == 0:
                if current not in seen:
                    self.ans = current
                    self.found = True
                return

            for char in chars:
                generate_permutations(chars, n - 1, current + char)

        n = len(nums[0])

        generate_permutations(["0", "1"], n)

        return self.ans


class TestSolution(unittest.TestCase):
    def test_findDifferentBinaryString(self):
        solution = Solution()
        self.assertTrue(solution.findDifferentBinaryString(["01", "10"]) in ["11", "00"])


if __name__ == '__main__':
    unittest.main()
