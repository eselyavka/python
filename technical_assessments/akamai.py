#!/usr/bin/env python

# Check if host belong to specific network,
# network and broadcast addresses are not included
# 10.10.0.0/255.255.255.192 or in cidr 10.10.0.0/26

import unittest


class Solution(object):
    def __init__(self):
        self.network = '10.10.0.'
        self.hosts_in_network = [self.network + str(host) for host in range(1, 63)]

    def is_belong(self, host):
        return host in self.hosts_in_network


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_is_in_network(self):
        self.assertTrue(all([self.solution.is_belong(host) for host in ['10.10.0.1',
                                                                        '10.10.0.34',
                                                                        '10.10.0.62']]))

    def test_is_not_in_network(self):
        self.assertFalse(True in [self.solution.is_belong(host) for host in ['10.10.0.0',
                                                                             '10.10.0.63',
                                                                             '192.168.0.1',
                                                                             '8.8.8.8',
                                                                             '127.0.0.1']])


if __name__ == '__main__':
    unittest.main()
