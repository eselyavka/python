#!/usr/bin/env python

import unittest


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return '[.]'.join(address.split('.'))


class TestSolution(unittest.TestCase):

    def test_defangIPaddr(self):
        solution = Solution()
        self.assertEqual(solution.defangIPaddr('1.1.1.1'), '1[.]1[.]1[.]1')


if __name__ == '__main__':
    unittest.main()
