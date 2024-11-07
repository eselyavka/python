#!/usr/bin/env python

import unittest

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        if B in A:
            return 1

        if set(B) - set(A):
            return -1

        is_substring = False
        i = 1
        _A = A

        while len(A) <= 10000 or is_substring:
            is_substring = B in A
            if is_substring:
                break
            else:
                A += _A
                i += 1

        return i if is_substring else -1

    def repeatedStringMatch2(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if B in A:
            return 1

        if set(B) - set(A):
            return -1

        cnt = 1
        A_ = A

        if len(A) <= len(B):
            while len(A) < 2 * len(B):
                if B in A:
                    return cnt
                A += A_
                cnt += 1
        else:
            while cnt <= len(B):
                if B in A:
                    return cnt
                A += A_
                cnt += 1

        return -1 if B not in A else cnt


class TestSolution(unittest.TestCase):
    def test_repeatedStringMatch(self):
        solution = Solution()
        self.assertEqual(solution.repeatedStringMatch("abcd", "cdabcdab"), 3)
        self.assertEqual(solution.repeatedStringMatch("abc", "cabcabca"), 4)
        self.assertEqual(solution.repeatedStringMatch("aaaaaaaaaaaaaaaab", "ba"), 2)
        self.assertEqual(solution.repeatedStringMatch2("abcd", "cdabcdab"), 3)
        self.assertEqual(solution.repeatedStringMatch2("abc", "cabcabca"), 4)
        self.assertEqual(solution.repeatedStringMatch2("aaaaaaaaaaaaaaaab", "ba"), 2)


if __name__ == '__main__':
    unittest.main()
