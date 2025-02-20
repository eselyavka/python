#!/usr/bin/env python

import unittest


class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        ans = []
        seen = set(nums)

        def generate_permutations(chars, n, current=""):
            if n == 0:
                if current not in seen:
                    ans.append(current)
                return
            for char in chars:
                generate_permutations(chars, n - 1, current + char)

        n = len(nums[0])

        generate_permutations(["0", "1"], n)

        return "" if not ans else ans.pop()


class TestSolution(unittest.TestCase):
    def test_findDifferentBinaryString(self):
        solution = Solution()
        self.assertTrue(solution.findDifferentBinaryString(["01", "10"]) in ["11", "00"])


if __name__ == '__main__':
    unittest.main()
