#!/usr/bin/python

import unittest


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def backtrack(idx, acc, data):
            if len(acc) == len(digits):
                data.append("".join(acc[:]))
                return

            for c in mapping[digits[idx]]:
                acc.append(c)
                backtrack(idx + 1, acc, data)
                acc.pop()

        ans = []
        local_res = []

        backtrack(0, local_res, ans)

        return ans


class TestSolution(unittest.TestCase):

    def test_letterCombinations(self):
        solution = Solution()

        self.assertEqual(sorted(solution.letterCombinations('23')),
                         ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self.assertEqual(sorted(solution.letterCombinations('')), [])
        self.assertEqual(sorted(solution.letterCombinations('4')), ['g', 'h', 'i'])


if __name__ == '__main__':
    unittest.main()
