#!/usr/bin/env python

import unittest


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        seen = set()
        res = ''
        for c in letters:
            if c not in seen:
                res += c
                seen.add(c)

        l = 0
        r = len(res)

        while l < r:
            mid = (l+r)//2
            if ord(res[mid]) == ord(target):
                break
            elif ord(target) > ord(res[mid]):
                l += 1
            else:
                r -= 1

        if res[mid] > target:
            return res[mid]
        else:
            if mid < len(res) - 1:
                return res[mid+1]
            return res[0]


class TestSolution(unittest.TestCase):
    def test_nextGreatestLetter(self):
        solution = Solution()
        self.assertEqual(solution.nextGreatestLetter(["c", "f", "j"], "a"), "c")
        self.assertEqual(solution.nextGreatestLetter(["c", "f", "j"], "z"), "c")
        self.assertEqual(solution.nextGreatestLetter(["c", "f", "j"], "c"), "f")
        self.assertEqual(solution.nextGreatestLetter(["c", "f", "j"], "d"), "f")
        self.assertEqual(solution.nextGreatestLetter(["c", "f", "j"], "g"), "j")
        self.assertEqual(solution.nextGreatestLetter(["c", "f", "j"], "j"), "c")
        self.assertEqual(solution.nextGreatestLetter(["c", "f", "j"], "k"), "c")
        self.assertEqual(solution.nextGreatestLetter(["e", "e", "e", "e", "e", "e",
                                                      "n", "n", "n", "n"], "n"), "e")


if __name__ == '__main__':
    unittest.main()
