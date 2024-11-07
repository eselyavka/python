#!/usr/bin/env python

import unittest


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid_part(s):
            return len(s) == 1 or (s[0] != '0' and int(s) < 256)

        result, parts = [], [None] * 4
        for i in range(1, min(len(s), 4)):
            parts[0] = s[:i]
            if is_valid_part(parts[0]):
                for j in range(1, min(len(s) - i, 4)):
                    parts[1] = s[i:i+j]
                    if is_valid_part(parts[1]):
                        for k in range(1, min(len(s) - i - j, 4)):
                            parts[2], parts[3] = s[i + j: i + j + k], s[i + j + k:]
                            if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                                result.append('.'.join(parts))

        return result


class TestSolution(unittest.TestCase):

    def test_restoreIpAddresses(self):
        solution = Solution()
        self.assertListEqual(solution.restoreIpAddresses("25525511135"),
                             ["255.255.11.135", "255.255.111.35"])


if __name__ == '__main__':
    unittest.main()
