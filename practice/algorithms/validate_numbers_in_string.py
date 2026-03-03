#!/usr/bin/env python3

"""Module for practice.algorithms.validate_numbers_in_string."""

import unittest


class Solution:
    def validateNums(self, s):
        """
        Will validate numbers in random string
        """
        nums = []
        n = len(s)
        idx = 0

        def is_num_starts(i):
            if i >= n:
                return False

            if s[i].isdigit():
                return True

            if s[i] == '.' and i + 1 < n and s[i + 1].isdigit():
                return True

            if s[i] == '-' and i + 1 < n and (i == 0 or s[i - 1] != '-'):
                j = i + 1
                if s[j].isdigit():
                    return True
                if s[j] == '.' and j + 1 < n and s[j + 1].isdigit():
                    return True

            return False

        while idx < n:
            if not is_num_starts(idx):
                idx += 1
                continue

            start = idx
            if s[idx] == '-':
                idx += 1
            seen_digit = False
            seen_dot = False
            while idx < n and (s[idx].isdigit() or s[idx] == "."):
                if s[idx].isdigit():
                    seen_digit = True
                else:
                    if seen_dot:
                        if start is not None and seen_digit:
                            token = s[start:idx]
                            nums.append(token.rstrip('.'))
                        while idx < n and (s[idx].isdigit() or s[idx] == "."):
                            idx += 1
                        start = None
                        break
                    seen_dot = True
                idx += 1

            if start is not None and seen_digit:
                nums.append(s[start:idx])

        return nums


class TestSolution(unittest.TestCase):
    def test_validateNums(self):
        solution = Solution()
        self.assertEqual(solution.validateNums("a1b2.3c--4d5..6"), ["1", "2.3", "4", "5"])


if __name__ == '__main__':
    unittest.main()
